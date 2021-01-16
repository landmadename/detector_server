from flask import Flask
from flask import request
import time
from detect import detect

app = Flask(__name__)
ALLOWED_EXTENSIONS = {'png',}

def allowed_file(filename):
    return '.' in filename \
        and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS \
            and filename.startswith("wx")

@app.route('/', methods=['GET', 'POST'])
def detector():
    if request.method == 'POST':
        file = request.files['file']
        file.save('C:\\CODE\\python\\TEMP\\detector_server\\imgs\\file.png')
        if file and allowed_file(file.filename):
            return detect()
    return "hi"