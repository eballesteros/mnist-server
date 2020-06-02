import tensorflow as tf

def create_simple_model():
    '''
    Create simple mnist model
    '''
    inputs = tf.keras.Input(shape=(28, 28, 1), name='inputs')
    
    x = tf.keras.layers.Conv2D(filters=8, kernel_size=3, strides=2, activation='relu', name='conv_1')(inputs)
    x = tf.keras.layers.Flatten(name='flatten')(x)
    outputs = tf.keras.layers.Dense(10, activation='softmax', name='outputs')(x)
    
    return tf.keras.Model(inputs=inputs, outputs=outputs, name='mnist_model')