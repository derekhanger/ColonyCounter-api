from flask import Flask, request
from flask_cors import CORS
from requests_toolbelt.multipart import decoder
import requests
import base64
import io
import Image

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'index'


@app.route('/upload', methods = ['POST'])
def upload():

    img = request.files['imageFile']


    return 'uploaded file'


if __name__ == "__main__":
    app.run(debug=True)
