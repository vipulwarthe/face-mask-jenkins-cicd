import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from keras.models import load_model
import numpy as np
from flask import Flask, redirect, url_for, request, render_template, jsonify
from PIL import Image

# os.environ["FLASK_ENV"] = "development"    # Creating A Devlopment Environment

app = Flask(__name__,template_folder='templates/')       # Initilize App
# port = 5000           # Setting Port Number

# #Setting an auth token allows us to open multiple tunnels at the same time
# ngrok.set_auth_token("22m1k05FJ4yE6oKKMz1aUShlBvX_6CiGv4wP95U7pvddczArE")

# # Open a ngrok tunnel to the HTTP server
# public_url = ngrok.connect(port).public_url
# print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}\"".format(public_url, port))

# # Update any base URLs to use the public ngrok URL
# app.config["BASE_URL"] = public_url


# load the pre-trained Keras model
model = load_model('Mask_detection_model.h5')


@app.route('/')
def index():
    # Main page
    return render_template('index1.html')  #Rendering Our Main Template

@app.route('/predict', methods=['POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        image = Image.open(request.files['file'].stream)     # Opening Uploaded File
        image = image.resize((224,224))                      # Resizing Image Based On Model Requirement
        image = img_to_array(image)                          # Changing Image to Array of pixels
        image = preprocess_input(image)                      # Preprocessing Image
        image=np.expand_dims(image, axis=0)                 

        
        predictions=model.predict(image)     # Predicting on Test Image
        predictions=predictions.reshape(-1)
        threshold=0.5
        y_pred=np.where(predictions >= threshold, 'Non Mask','Mask')
        result = y_pred[0]
        
        print('[PREDICTED CLASSES]: {}'.format(y_pred))
        print('[RESULT]: {}'.format(result))

        return result


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
  #  Start the Flask server in a new thread
#   threading.Thread(target=app.run, kwargs={"use_reloader": False}).start()
