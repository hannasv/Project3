import tensorflow as tf
import numpy as np


def nn_model(X, input_size, hidden_sizes, output_size, stddev):
    X = tf.cast(X, tf.float32)
    # Define weights and biases
    # (Using normal distribution)

    # 1) set up parameters
    w = []
    b = []
    layer = []


    # 2) APPEND ALL THE LAYERS

    # Input layer
    #w.append(tf.Variable(tf.random.normal([input_size, hidden_sizes[0]],
                                       #mean=0.0,
                                       #stddev=1.0,
                                       #dtype=tf.float32,
                                       #seed=None,
                                       #name=None
     #                                  )))

    b.append(tf.Variable(tf.zeros(hidden_sizes[0])))

    w.append(tf.Variable(tf.truncated_normal([input_size, hidden_sizes[0]], stddev)))
    #b.append(tf.Variable(tf.constant(0.1 if neuron_fn in [tf.nn.relu, tf.nn.relu6] else 0.0, shape=b_dims)))

    # add hidden layers (variable number)
    for i in range(1, len(hidden_sizes)):
        #w.append(tf.Variable(tf.random_normal([hidden_sizes[i - 1], hidden_sizes[i]], stddev=0.1)))
        w.append(tf.Variable(tf.truncated_normal([hidden_sizes[i - 1], hidden_sizes[i]], stddev)))
        b.append(tf.Variable(tf.zeros([hidden_sizes[i]])))


    # Output layer
    #w.append(tf.Variable(tf.random.normal([hidden_sizes[-1], output_size],
     #                                  mean=0.0,
      #                                 stddev=1.0,
       #                                dtype=tf.float32,
        #                               seed=None,
         #                              name=None
          #                             )))

    b.append(tf.Variable(tf.ones(output_size)))
    w.append(tf.Variable(tf.truncated_normal([hidden_sizes[-1], output_size], stddev)))

    # 3) DEFINE MODEL

    layer.append(tf.nn.elu(tf.matmul(X, w[0]) + b[0]))

    for i in range(1, len(hidden_sizes)):
        layer.append(tf.nn.elu(tf.matmul(layer[i - 1], w[i]) + b[i]))

    output = tf.matmul(layer[-1], w[-1]) + b[-1]

    return output


