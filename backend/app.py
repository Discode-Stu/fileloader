import os
from flask import Flask, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')



UPLOAD_FOLDER = '/Volumes/DStuartHD/Code/rykeCodingChallenge/backend/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


CORS(app)
# cors = CORS(app, resources={
#   r"/*": {
#     "origins": "*"
#   }
# })

@app.route('/', methods=['GET'])
def home_page():
      content = 'Hello world'
      return content
 

@app.route('/upload', methods=['POST'])
def fileUpload():
    target=os.path.join(UPLOAD_FOLDER,'test_docs')
    if not os.path.isdir(target):
        os.mkdir(target)
    logger.info("welcome to upload`")
    file = request.files['file'] 
    filename = secure_filename(file.filename)
    destination="/".join([target, filename])
    file.save(destination)
    session['uploadFilePath']=destination
    response=destination
    return response

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True,port=5000,use_reloader=False)
    # app.run(debug=True,host="0.0.0.0",use_reloader=False)


flask_cors.CORS(app, expose_headers='Authorization')