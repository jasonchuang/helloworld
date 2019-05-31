import tensorflow as tf

from tensorflow.python.saved_model import tag_constants
from tensorflow.python.saved_model.signature_def_utils_impl import predict_signature_def

if __name__ == "__main__":
    x = tf.placeholder(tf.float32, [None, 4], name="myInput")
    keys_placeholder = tf.placeholder(tf.string, shape=[None])
    y = tf.multiply(x, 2.0)

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    builder = tf.saved_model.builder.SavedModelBuilder("./simple_saved_model")
    keys = tf.identity(keys_placeholder)
    signature = predict_signature_def(inputs={'keys': keys_placeholder, 'myInput': x },
            outputs={'keys': keys, 'myOutput': y })
    builder.add_meta_graph_and_variables(sess=sess, tags=[tag_constants.SERVING], signature_def_map={'predict': signature})
    builder.save()

    sess.close()

