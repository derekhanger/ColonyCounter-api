from flask import Flask, request
from flask_cors import CORS
from requests_toolbelt.multipart import decoder
import requests
import base64
import io
from PIL import Image
from scipy import countingFunction
import os
import io
import Image
from array import array

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'index'


@app.route('/upload', methods = ['POST'])
def upload():
    
    img = request.files['imageFile']
    with open('assets/file.temp', 'w') as f:
        f.write(img)

    def readimage(path):
        with open(path, "rb") as f:
            return bytearray(f.read())

    bytez = readimage('assets/file.temp')

    image = Image.open(io.BytesIO(bytez))
    image.save("assets/picture.png")

    return 'uploaded file'


@app.route('/getCount', methods = ['GET'])
def getCount():
    pass

if __name__ == "__main__":
    app.run(debug=True)
