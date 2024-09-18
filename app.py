from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)