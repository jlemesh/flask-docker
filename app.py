from flask import Flask
from flask import request
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import preprocess_input, decode_predictions
import numpy as np
from PIL import Image

app = Flask(__name__) # initialize flask app
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 # set max uploaded image size to 5 MB
app.inception = InceptionV3(weights='imagenet') # initialize inception v3 model in advance to avoid loading it for each request

# index page
@app.route('/')
def index():
  return 'API for image classification using Inception V3 model. POST /predict with image file to get predictions.'

# predict image class using inception v3 model
@app.route('/predict', methods=['POST'])
def predict():
  file = request.files['file']
  app.logger.info('submitted file for prediction: %s: content length: %s, content type: %s', file.filename, file.content_type)

  img = Image.open(file).resize((299, 299)) # resize for inception v3 model accepted size
  x = image.img_to_array(img)
  x = np.expand_dims(x, axis=0)
  x = preprocess_input(x)
  
  preds = app.inception.predict(x) # predict image classes (returna a 1000 length array of probabilities)
  decoded_preds = decode_predictions(preds, top=3)[0] # decode top 3 predictions
  response = {
    'predictions': []
  }
  for pred in decoded_preds:
    response['predictions'].append({
      'class': pred[1],
      'probability': float(pred[2])
    })
  app.logger.info('prediction result: %s', response)

  return response
