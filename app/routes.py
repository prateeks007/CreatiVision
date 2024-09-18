import logging
from flask import render_template, request, jsonify
from app import app
from app.banner import generate_banner
from app.video import generate_video
from app.utils import allowed_file, save_uploaded_file
from app.test import generate_and_save_banner

@app.route('/')
@app.route('/banner')
@app.route('/video')
def index():
    return render_template('index.html')

@app.route('/generate_banner', methods=['POST'])
def generate_banner_route():
    try:
        if 'productImage' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        file = request.files['productImage']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        
        offer = request.form['offer']
        theme = request.form['theme']
        color_palette = request.form['colorPalette'].split(',')

        result = generate_and_save_banner(file, offer, theme, color_palette)
        return jsonify(result)
    except Exception as e:
        logging.error(f"Error in generate_banner_route: {str(e)}", exc_info=True)
        return jsonify({'error': str(e)}), 500

@app.route('/generate_video', methods=['POST'])
def generate_video_route():
    if 'productImage' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['productImage']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = save_uploaded_file(file)
        offer = request.form['offer']
        theme = request.form['theme']
        color_palette = request.form['colorPalette'].split(',')
        size = tuple(map(int, request.form['size'].split('x')))
        duration = int(request.form['duration'])
        
        video_path = generate_video(filename, offer, theme, color_palette, size, duration)
        return jsonify({'video': video_path})
    return jsonify({'error': 'Invalid file type'}), 400
