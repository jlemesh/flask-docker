FROM python:3.11.9-bullseye as flask

WORKDIR /app

RUN mkdir uploads

ENV FLASK_PORT=3000

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD flask run --host=0.0.0.0 --port=${FLASK_PORT}
