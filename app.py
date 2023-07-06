from io import BytesIO

import flask
from PIL import Image
from flask import Flask, send_file
from flask_cors import CORS
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from torchvision.models.detection import ssd300_vgg16

from detect import run_detection

app = Flask(__name__)
CORS(app)


def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')


@app.get("/")
def hello_world():
    return "Hello, World!"


@app.post("/detect")
def detect():
    model = flask.request.form.get('model', 'fasterrcnn_resnet50')
    imagefile = flask.request.files.get('file[]', '')
    img = Image.open(imagefile)
    object_detection_model = None
    if model == 'fasterrcnn_resnet50':
        object_detection_model = fasterrcnn_resnet50_fpn(pretrained=True, progress=False)
    elif model == 'ssd300_vgg16':
        object_detection_model = ssd300_vgg16(pretrained=True, progress=False)
    output_img = run_detection(img, object_detection_model)
    return serve_pil_image(output_img)
