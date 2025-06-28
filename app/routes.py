from flask import render_template, request, jsonify
from google.api_core.exceptions import Forbidden, ResourceExhausted
from app import app
from app.huggingfacetti import generate_and_save_banner
import logging

@app.route('/')
@app.route('/banner')
def index():
    return render_template('index.html')

@app.route('/generate_banner', methods=['POST'])
def generate_banner_route():
    files = request.files.getlist('productImages')
    offer = request.form.get('offer')
    theme = request.form.get('theme')
    color_palette = request.form.get('colorPalette', '').split(',')
    generator_type = request.form.get('generatorType')
    size = request.form.get('size')
    fmt = request.form.get('format', 'PNG')

    if not files or not offer or not theme or not color_palette or not generator_type:
        return jsonify({'error': 'Missing required fields'}), 400  # BAD REQUEST

    params = {
        'files': files,
        'offer': offer,
        'theme': theme,
        'color_palette': color_palette,
        'generator_type': generator_type,
        'format': fmt
    }

    if size:
        try:
            params['size'] = tuple(map(int, size.split('x')))
        except ValueError:
            return jsonify({'error': 'Invalid size format, expected WIDTHxHEIGHT'}), 400

    try:
        result = generate_and_save_banner(**params)
        if not isinstance(result, dict):
            result = {'error': 'Unexpected result from generate_and_save_banner'}
            return jsonify(result), 500  # SERVER ERROR
        if "error" in result:
            return jsonify(result), 500
        return jsonify(result), 200

    except Forbidden as fe:
        logging.error("[Generate Banner Forbidden]: %s", fe)
        return jsonify({
            'error': 'Google API forbidden – billing might be disabled',
            'details': str(fe)
        }), 403  # FORBIDDEN

    except ResourceExhausted as rexc:
        logging.error("[Generate Banner Quota Exceeded]: %s", rexc)
        return jsonify({
            'error': 'Quota exhausted on text-generation model',
            'details': str(rexc)
        }), 429  # TOO MANY REQUESTS

    except Exception as e:
        logging.exception("[Generate Banner Error]")
        return jsonify({
            'error': 'An unexpected error occurred while generating the banner.',
            'details': str(e)
        }), 500
