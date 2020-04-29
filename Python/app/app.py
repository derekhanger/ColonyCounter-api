from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route('/upload', methods = ['POST'])
def upload():
    file = request.files['image']
    if(file):
        print("uploaded")
    


if __name__ == "__main__":
    app.run(debug=True)
