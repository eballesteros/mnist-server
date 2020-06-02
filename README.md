# MNIST Server

Through-out this repo, it will be assumed you have Docker installed. If you don't, please install it before proceeding.

## Training

Once you've cloned the repo, you can train the model running:

```bash
docker run -v /path/to/mnist-server:/app tensorflow/tensorflow:2.1.0-py3 python /app/train.py
```

*Note:* If you have a GPU available, you can use the `tensorflow/tensorflow:2.1.0-gpu-py3` image instead. You will need to add `--runtime=nvidia` or `--gpus all` to you `docker run` command, depending on your Docker version (Check https://www.tensorflow.org/install/docker#tensorflow_docker_requirements)

## Serving

We are going to use TensorFlow Serving instead of building the typical flask backend. This allows for easy implementation of a high performance backend, supporting for example gRPC and mini-batching.

We'll also use docker-compose to seamlessly bring up the server, the client, and stablish the connections between them. To start both services, navigate to `path/to/mnist-server` and run:

```bash
docker-compose up
```

Once the boot-up finishes, you should have a jupyter notebook that will act as a client running on `http://localhost:8888/notebooks/mnist-server/client.ipynb`. Use token `letmein` to access.

*Note*: The first time you run it, it may take some time to pull the images.
