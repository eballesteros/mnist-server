# MNIST Server

Through-out this repo, it will be assumed you have Docker installed. If you don't, please install it before proceeding.

## Training

Once you've cloned the repo, you can train the model running:

```bash
docker run  docker run -v /path/to/mnist-server:/app tensorflow/tensorflow:2.1.1 python /app/train.py
```

*Note:* If you have a GPU available, you can use the `tensorflow/tensorflow:2.1.1-gpu` image instead. You will need to add `--runtime=nvidia` or `--gpus all` to you `docker run` command, depending on your Docker version (Check https://www.tensorflow.org/install/docker#tensorflow_docker_requirements)