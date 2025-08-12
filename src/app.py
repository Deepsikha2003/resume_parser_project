import os
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from parser import parse_resume

app = Flask(__name__)

# Configure a temporary upload folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    """
    Serves the main HTML page for the user interface.
    """
    return render_template('index.html')

@app.route('/parse', methods=['POST'])
def parse_uploaded_resume():
    """
    API endpoint to receive a resume file and return parsed data.
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        try:
            parsed_data = parse_resume(file_path)
            os.remove(file_path)
            return jsonify(parsed_data)
        except Exception as e:
            if os.path.exists(file_path):
                os.remove(file_path)
            return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)