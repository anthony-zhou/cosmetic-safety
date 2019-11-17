from flask import Flask, render_template, request, redirect, send_from_directory
from letsjson import getjson
import os

app = Flask("cosmetic-safety")

@app.route('/')
def upload_file():
    return render_template('/upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        full_filename = "/Users/nathaniel/PycharmProjects/cosmetic-safety/" + f.filename
        myjson = getjson(full_filename)
        htmlstr = "<table><tr><td>Chemical</td><td>Harmfulness</td>"
        fillstr = ""
        for chemical in myjson:
            fillstr += "<tr>"
            fillstr += "<td>"
            fillstr += chemical
            fillstr += "</td>"
            fillstr += "<td>"
            fillstr += myjson[chemical]
            fillstr += "</td>"
            fillstr += "</tr>"

        if fillstr == "":
            return "Hooray! Your product is just fine!"
        else:
            return htmlstr + fillstr + "</table"


@app.route('/<path:filename>')
def send_file(filename):
    return send_from_directory('/', filename)


if __name__ == "__main__":
    app.run()



