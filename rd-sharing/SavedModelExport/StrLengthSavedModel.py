import tensorflow as tf

from tensorflow.python.saved_model import tag_constants
from tensorflow.python.saved_model.signature_def_utils_impl import predict_signature_def

def resize(str_tensor):
    # str_tensor here is shape=()
    return tf.strings.length(str_tensor)

if __name__ == "__main__":
    # x is shape=(?,), means string list to fit ML Engine batch input
    x = tf.placeholder(tf.string, shape=[None], name="myInput")
    # output y is shape=(?,) as well and dtype is int32
    y = tf.map_fn(resize, x, back_prop=False, dtype=tf.int32)
    
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    builder = tf.saved_model.builder.SavedModelBuilder("./str_length_saved_model")
    signature = predict_signature_def(inputs={'myInput': x }, outputs={'myOutput': y })
    builder.add_meta_graph_and_variables(sess=sess, tags=[tag_constants.SERVING], signature_def_map={'predict': signature})
    builder.save()

    sess.close()

