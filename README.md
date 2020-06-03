# MNIST Server

This repo is a demo on how to easily train a simple deep model for MNIST classification and deploy it. We will use `TensorFlow 2.1.0` for training, `TensorFlow serving` for the deployment, and `docker-compose` for orchestration and to abstract most of the complexity.

Throughout this repo, it will be assumed that you have Docker installed. If you don't, please install it before proceeding.

## Training

We are going to train a simple model with just 1 convolutional and 1 fully-connected layers. To do so, once you've cloned the repo, you can simply run:

```bash
docker run -v /path/to/mnist-server:/app tensorflow/tensorflow:2.1.0-py3 python /app/train.py
```

This instruction will run train.py in a tensorflow docker container, train the model and save it into `./model_files/1`. With this simple architecture we can get over 97% accuracy on the validation set.

*Note1:* The first time you run it, it may take some time to pull the docker image. After that it should be reasonably fast.

*Note2:* If you have a GPU available, you can use the `tensorflow/tensorflow:2.1.0-gpu-py3` image instead. You will need to add `--runtime=nvidia` or `--gpus all` to you `docker run` command, depending on your Docker version (Check <https://www.tensorflow.org/install/docker#tensorflow_docker_requirements)>

## Deployment

Now lets deploy the model: We are going to use TensorFlow Serving instead of building the typical Flask backend. This allows for easy implementation of a high performance backend, supporting for example gRPC and mini-batching.

We'll also use docker-compose to seamlessly bring up the server, the client, and establish the connections between them. To start both services, navigate to `path/to/mnist-server` and run:

```bash
docker-compose up
```

Once the boot up finishes, you should have a jupyter notebook that will act as a client running on your machines <localhost:8888/notebooks/mnist-server/client.ipynb> Use token `letmein` to access.

*Note*: The first time you run it, it may take some time to pull the images.
