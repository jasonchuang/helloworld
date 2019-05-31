import tensorflow as tf

from tensorflow.python.saved_model import tag_constants
from tensorflow.python.saved_model.signature_def_utils_impl import predict_signature_def

def resize(str_tensor):
    print ("resize begins")
    decoded_jpeg = tf.image.decode_jpeg(str_tensor, ratio=2, channels=3)
    print (decoded_jpeg)
    encoded_jpeg = tf.image.encode_jpeg(decoded_jpeg)
    print (encoded_jpeg)
    return tf.encode_base64(encoded_jpeg, pad=True)

if __name__ == "__main__":
    x = tf.placeholder(tf.string, shape=[None], name="myInput")
    print (x)
    print ("The following is map fn")
#    y = tf.map_fn(resize, x, back_prop=False, dtype=tf.uint8)
    y = tf.map_fn(resize, x, back_prop=False)
    print ("The following is Y")
    print (y)
    
#    y = tf.string.length(x)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    builder = tf.saved_model.builder.SavedModelBuilder("./resize_saved_model")
    signature = predict_signature_def(inputs={'myInput': x },
            outputs={'myOutput': y })
    builder.add_meta_graph_and_variables(sess=sess, tags=[tag_constants.SERVING], signature_def_map={'predict': signature})
    builder.save()

    sess.close()

