import os
from flask_dropzone import Dropzone
from flask import Flask, render_template, request

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

app = Flask(__name__)
app.config.update(
    # UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    DROPZONE_MAX_FILE=1024,
    DROPZONE_TIMEOUT=5*60*1000)

dropzone: Dropzone = Dropzone(app)