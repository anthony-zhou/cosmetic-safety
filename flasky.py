from flask import Flask, render_template, request, redirect, send_from_directory
import os

app = Flask("cosmetic-safety")

@app.route('/')
def upload_file():
    os.makedirs(os.path.join(app.instance_path, 'htmlfi'), exist_ok=True)
    return render_template('/upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        full_filename = "/Users/nathaniel/PycharmProjects/cosmetic-safety/" + f.filename
        return render_template("imagereturn.html", user_image=full_filename)

@app.route('/<path:filename>')
def send_file(filename):
    return send_from_directory('/', filename)


if __name__ == "__main__":
    app.run()



