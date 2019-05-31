import cv2
import numpy as np
import NLDF
import os
import sys
import tensorflow as tf
import time
import vgg16

from tensorflow.python.saved_model import tag_constants
from tensorflow.python.saved_model.signature_def_utils_impl import predict_signature_def

height = 352
width = 352
channels = 3

def decode_and_resize(image_str_tensor):
    """Decodes jpeg string, resizes it and returns a uint8 tensor."""
    image = tf.image.decode_jpeg(image_str_tensor, channels=channels)
    # Note resize expects a batch_size, but tf_map supresses that index,
    # thus we have to expand then squeeze.  Resize returns float32 in the
    # range [0, uint8_max]
    image = tf.expand_dims(image, 0)
    image = tf.image.resize_bilinear(image, [height, width], align_corners=False)
    image = tf.squeeze(image, squeeze_dims=[0])
    image = tf.cast(image, dtype=tf.uint8)
    return image

def reshape_and_encode(prob_tensor):
    encoded_image = tf.reshape(prob_tensor, (176, 176, 2))
    split, _ = tf.split(encoded_image, 2, 2)
    encoded_image = tf.image.convert_image_dtype(split, dtype=tf.uint8)
    encoded_image = tf.image.encode_png(encoded_image, compression=1)
    b64_image = tf.encode_base64(encoded_image, pad=True)
    return b64_image

if __name__ == "__main__":
    model = NLDF.Model()
    keys_placeholder = tf.placeholder(tf.string, shape=[None])
    b64_str = tf.placeholder(tf.string, name='input_string', shape=[None])

    image = tf.map_fn(decode_and_resize, b64_str, back_prop=False, dtype=tf.uint8)
    # cast to float32 to fit input_holder, but is still in range [0, uint8_max]
    image = tf.cast(image, dtype=tf.float32)
    model.input_holder = tf.reshape(image, (1, 352, 352, 3))

    model.build_model()

    encodedImage = reshape_and_encode(model.Prob)
    tf.identity(encodedImage, name="b64_output")

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())
    ckpt = tf.train.get_checkpoint_state('model_nldf/')
    saver = tf.train.Saver()
    saver.restore(sess, ckpt.model_checkpoint_path)

    builder = tf.saved_model.builder.SavedModelBuilder("./nldf_saved_model")
    keys = tf.identity(keys_placeholder)
    signature = predict_signature_def(inputs={'keys': keys_placeholder, 'input_string': b64_str },
            outputs={'keys': keys, 'b64_output': encodedImage })
    builder.add_meta_graph_and_variables(sess=sess, tags=[tag_constants.SERVING], signature_def_map={'predict': signature})
    builder.save()

    sess.close()

