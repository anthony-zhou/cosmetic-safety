from flask import Flask
from imaging import text_words
from toxic import gettoxicity

app = Flask("cosmetic-safety")

@app.route('/')
def hello_world():
    return str(gettoxicity('formaldehyde'))





