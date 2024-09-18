import os
from werkzeug.utils import secure_filename
import logging

UPLOAD_FOLDER = 'uploads'

GENERATED_FOLDER = 'generated'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_uploaded_file(file):
    filename = secure_filename(file.filename)
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)
    logging.info(f"File saved at: {file_path}")
    return file_path

def save_generated_file(file_content, filename, file_type):
    if not os.path.exists(GENERATED_FOLDER):
        os.makedirs(GENERATED_FOLDER)
    file_path = os.path.join(GENERATED_FOLDER, f"{file_type}_{filename}")
    with open(file_path, 'wb') as f:
        f.write(file_content)
    return file_path
