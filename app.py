import base64

from flask import Flask, render_template, request, redirect, send_from_directory
from letsjson import getjson

from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)

@app.route('/')
def upload_file():
    return render_template('/upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        full_filename = "/Users/nathaniel/PycharmProjects/cosmetic-safety/imageToSave.png"
        myjson = getjson(full_filename)

        return render_template("resultstable.html", chemicals=myjson)

@app.route('/uploadee', methods=['GET', 'POST'])
def uploader_filee():
    if request.method == 'POST':
        print(request.data)
        img_data = request.data[22:]
        print(img_data)
        with open("imageToSave.png", "wb") as fh:
            fh.write(base64.decodebytes(img_data))
        full_filename = "/Users/nathaniel/PycharmProjects/cosmetic-safety/imageToSave.png"
        myjson = getjson(full_filename)

        return render_template("resultstable.html", chemicals=myjson)

@app.route('/<path:filename>')
def send_file(filename):
    return send_from_directory('/', filename)



if __name__ == "__main__":
    app.run(debug=True)



