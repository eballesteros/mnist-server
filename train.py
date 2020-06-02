import os
import tensorflow as tf
print(f'Using tf {tf.__version__}')

from model_src.simple_model import create_simple_model

EPOCHS = 5
BS = 32
MODELS_REL_DIR = 'model_files'
VERSION = 1

def create_ds(images, labels, bs=32):
    '''
    '''
    return tf.data.Dataset.from_tensor_slices((images, labels)).batch(bs)

def get_datasets(bs=32):
    '''
    '''
    print('Loading and preprocessing data')

    # get data
    (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

    # normalize
    train_images = train_images / 255.0
    test_images = test_images / 255.0

    # reshape
    train_images = train_images.reshape(train_images.shape[0], 28, 28, 1)
    test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)

    # create datasets
    train_ds = create_ds(train_images, train_labels, bs=bs)
    test_ds = create_ds(test_images, test_labels, bs=bs)

    return train_ds, test_ds

def save_model(model, path):
    '''
    '''
    print(f'Saving model in {path}')

    tf.keras.models.save_model(
            model,
            path,
            overwrite=True,
            include_optimizer=True,
            save_format=None,
            signatures=None,
            options=None
        )


def main():
    # load and preprocess data
    train_ds, test_ds = get_datasets(BS)

    # create model
    model = create_simple_model()

    # train
    model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

    model.fit(train_ds, validation_data=test_ds, epochs=EPOCHS)

    # save
    save_model(model, os.path.join(os.path.dirname(os.path.realpath(__file__)), MODELS_REL_DIR, str(VERSION)))



if __name__ == '__main__':
    main()