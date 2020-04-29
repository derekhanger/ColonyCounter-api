from flask import Flask, request
from flask_cors import CORS
from requests_toolbelt.multipart import decoder
import requests

app = Flask(__name__)
CORS(app)


@app.route('/upload', methods = ['POST'])
def upload():
    testEnrollResponse = requests.post(...)
    multipart_data = decoder.MultipartDecoder.from_response(testEnrollResponse)

    for part in multipart_data.parts:
        print(part.content)  # Alternatively, part.text if you want unicode
        print(part.headers)
    


if __name__ == "__main__":
    app.run(debug=True)
