from flask import Flask, request, render_template, send_file
import os
from werkzeug.utils import secure_filename
from converters import (
    pdf_converter,
    docx_converter,
    image_converter,
    video_converter,
    audio_converter,
    excel_converter,
    powerpoint_converter,
    text_converter,
    html_converter,
    csv_converter
)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {
    'pdf', 'docx', 'xlsx', 'jpg', 'jpeg', 'png', 'mp4', 'mp3', 
    'pptx', 'txt', 'html', 'csv'
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_file():
    if 'file' not in request.files:
        return 'No file part', 400
    
    file = request.files['file']
    target_format = request.form.get('target_format')
    
    if file.filename == '':
        return 'No selected file', 400
    
    if not allowed_file(file.filename):
        return 'File type not allowed', 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Determine source format
        source_format = filename.rsplit('.', 1)[1].lower()
        
        # Convert file based on source and target formats
        try:
            converted_file = convert_file_format(filepath, source_format, target_format)
            return send_file(converted_file, as_attachment=True)
        except Exception as e:
            return f'Error converting file: {str(e)}', 500

def convert_file_format(filepath, source_format, target_format):
    # This will be implemented in the converters module
    pass

if __name__ == '__main__':
    app.run(debug=True) 