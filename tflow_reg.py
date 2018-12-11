import tensorflow as tf

def nn_model(X, n_nodes):

    X = tf.cast(X, tf.float32)
    # Define weights and biases
    # (Using normal distribution)
    w_1 = tf.Variable(tf.random.normal(n_nodes[0:2],
                                       mean=0.0,
                                       stddev=1.0,
                                       dtype=tf.float32,
                                       seed=None,
                                       name=None
                                       ))

    b_1 = tf.Variable(tf.ones(n_nodes[1]))


    # Define layer 1 and activation function

    layer_1 = tf.add(tf.matmul(X, w_1), b_1)
    # layer_1 = tf.nn.relu(layer_1)
    layer_1 = tf.nn.sigmoid(layer_1)
    layer_1 = tf.nn.relu(layer_1)


    # Multiply by layer 1 and add bias. Then activation function
    # Obtain layer 2

    w_2 = tf.Variable(tf.random.normal(n_nodes[1:3],
                                       mean=0.0,
                                       stddev=1.0,
                                       dtype=tf.float32,
                                       seed=None,
                                       name=None
                                       ))

    b_2 = tf.Variable(tf.ones(n_nodes[2]))

    layer_2 = tf.add(tf.matmul(layer_1, w_2), b_2)
    layer_2 = tf.nn.sigmoid(layer_2)



    # Multiply by layer 2 and add bias. Then activation function
    # Obtain output

    w_o = tf.Variable(tf.random.normal(n_nodes[2:4],
                                       mean=0.0,
                                       stddev=1.0,
                                       dtype=tf.float32,
                                       seed=None,
                                       name=None
                                       ))

    b_o = tf.Variable(tf.ones(n_nodes[3]))

    output = tf.add(tf.matmul(layer_2, w_o), b_o)

    return output



    # MSE

