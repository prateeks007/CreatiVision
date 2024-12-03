import logging
from flask import render_template, request, jsonify
from app import app
from app.banner import generate_banner
# from app.video import generate_video
from app.utils import allowed_file, save_uploaded_file
from app.huggingfacetti import generate_and_save_banner

@app.route('/')
@app.route('/banner')
# @app.route('/video')
def index():
    return render_template('index.html')

@app.route('/generate_banner', methods=['POST'])
def generate_banner_route():
    files = request.files.getlist('productImages')
    offer = request.form.get('offer')
    theme = request.form.get('theme')
    color_palette = request.form.get('colorPalette').split(',')
    generator_type = request.form.get('generatorType')
    size = request.form.get('size')
    format = request.form.get('format', 'PNG')

    if not files or not offer or not theme or not color_palette or not generator_type:
        return jsonify({'error': 'Missing required fields'}), 400

    banner_params = {
        'files': files,
        'offer': offer,
        'theme': theme,
        'color_palette': color_palette,
        'generator_type': generator_type,
        'format': format
    }

    if size:
        banner_params['size'] = tuple(map(int, size.split('x')))

    result = generate_and_save_banner(**banner_params)
    return jsonify(result)
