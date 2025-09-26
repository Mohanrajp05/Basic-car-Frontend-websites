from flask import Flask, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'website.html')

@app.route('/login.html')
def login():
    return send_from_directory('templates', 'login.html')

@app.route('/templates/<path:filename>')
def serve_template_files(filename):
    return send_from_directory('templates', filename)

@app.route('/index.html')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/Features.html')
def features():
    return send_from_directory('.', 'Features.html')

@app.route('/services.html')
def services():
    return send_from_directory('.', 'services.html')

@app.route('/contact us.html')
def contact():
    return send_from_directory('.', 'contact us.html')

@app.route('/<path:filename>')
def serve_static_files(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(debug=True, port=5000)