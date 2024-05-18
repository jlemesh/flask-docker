# flask-docker

A simple API for image classification using Inception V3 model. `POST` `/predict` with image file to get predictions.

## Usage

### Run

```bash
# TLDR; build and run app image
docker build -t flask . && docker run -it --rm --publish 3000:3000 --name flask flask

# build docker image
docker build -t flask .

# pull docker image from public registry
docker pull jlemesh/flask-docker

# run docker image that was built
docker run -it --publish 3000:3000 --name flask flask

# run pulled docker image
docker run -it --publish 3000:3000 --name flask jlemesh/flask-docker:latest

# run docker image on custom port (accessible on http://localhost:3005, image port 3001)
docker run -it --publish 3005:3001 --env FLASK_PORT=3001 flask
```

### Predict

Submit an image to make a prediction:

```bash
curl \
  -F "file=@dog.jpg" \
  http://localhost:3000/predict
```

## How this was created

1. Read [Flask documentation](https://flask.palletsprojects.com/en/3.0.x/quickstart/)
1. Install prerequisites if not already installed: Docker, python, venv
1. [Install](https://flask.palletsprojects.com/en/3.0.x/installation/) Flask: `pip install Flask`
1. Write a simple `app.py` file and make sure it runs using Flask command: `flask run`
1. Run `pip freeze` to create basic `requirements.txt` file
1. Create Dockerfile:
  - pick base python image
  - copy files/install packages/set `CMD` to run on container startup
  - add possibility to customize ports, both of container and host
1. Make sure image builds and runs on Docker:
  - fix typos
  - add `--host=0.0.0.0` to flask command as container IP is not 127.0.0.1 and connection is refused when accessing the app from localhost
1. Add `/predict` endpoint which accepts file upload
1. Add and install `tensorflow`, `numpy`
1. Write basic code to predict uploaded image class and return response to the client
1. Optimize the app so InceptionV3 is loaded on statup instead of each request
1. Push image to Docker hub as described in [Docker docs](https://docs.docker.com/get-started/04_sharing_app/)
