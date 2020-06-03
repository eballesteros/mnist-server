# MNIST Server

This repo is a demo on how to easily train and deploy a simple deep model for digit classification. The main goal is to make it as effortless as possible (just 2 commands after cloning!) to train and serve this model on either macOS, Linux or Windows. We will use `TensorFlow 2.1.0` for training, `TensorFlow serving` for the deployment, and `docker-compose` for orchestration and to abstract most of the complexity.

Throughout this repo, it will be assumed that you have Docker installed. If you don't, please install it before proceeding.

## Training

We are going to train a simple model with just 1 convolutional and 1 fully-connected layers. To do so, once you've cloned the repo, you can navigate to the projects root and simply run:

```bash
docker-compose -f train-compose.yml up
```

This instruction will start a tensorflow docker container and run train.py, training the model and saving it into `./model_files/1`. With this simple architecture we can get over 96% accuracy on the validation set.

*Note:* The first time you run it, it may take some time to pull the docker image. After that it should be reasonably fast.

## Deployment

Now lets deploy the model: We are going to use TensorFlow Serving instead of building the typical Flask backend. This allows for easy implementation of a high performance backend, supporting advanced features like gRPC or mini-batching, and opening the door tu super-high scalability using Kubeflow.

You can check (and modify) some server configuration parameters in `server_src/config`. Batch related parameters are very model/application/system dependent. You can check [this guide](https://github.com/tensorflow/serving/tree/master/tensorflow_serving/batching#batch-scheduling-parameters-and-tuning) to better understand how to tune them.

We'll also use docker-compose to seamlessly bring up the server, the client, and establish the connections between them. To start both services, navigate to the projects root and  and run:

```bash
docker-compose -f client-server-compose.yml up
```

Once the bootup finishes, you should have a jupyter notebook that will act as a client running on your machines <localhost:8888/notebooks/mnist-server/client.ipynb> Use token `letmein` to access.

*Note*: The first time you run it, it may take some time to pull the images.

## Next Steps

### GPU support

GPU support for both training and serving can be added with a few tweaks here and there.
