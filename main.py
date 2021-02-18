from flask import Flask
from flask import request
import time
import detect

app = Flask(__name__)
ALLOWED_EXTENSIONS = {'png',}

def allowed_file(filename):
    return '.' in filename \
        and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def detector():
    if request.method == 'POST':
        type_ = request.form['type']
        if type_ == "pic":
            file = request.files['file']
            file.save('./imgs/file.png')
            if file and allowed_file(file.filename):
                return detect.detect_pic()
    return "hi"