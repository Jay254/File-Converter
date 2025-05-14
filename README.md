# File Converter

A web-based file converter that supports conversion between the top 10 most common file formats.

## Features

- 🚀 Fast and efficient file conversion
- 🔒 Secure: Files are automatically deleted after conversion
- 💻 User-friendly web interface
- 📱 Responsive design
- 🔄 Supports multiple file formats
- ⚡ Real-time conversion status

## Supported Formats

- PDF (Portable Document Format)
- DOCX (Microsoft Word)
- XLSX (Microsoft Excel)
- JPG/PNG (Images)
- MP4 (Video)
- MP3 (Audio)
- PPTX (PowerPoint)
- TXT (Text)
- HTML
- CSV

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- Unix/MacOS:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Drag and drop a file or click to select a file
2. Choose the target format from the dropdown menu
3. Click "Convert File"
4. The converted file will be downloaded automatically

## Security

- All uploaded files are stored temporarily in the `uploads` directory
- Files are automatically deleted after conversion
- Maximum file size is limited to 16MB
- Only supported file formats are allowed

## Requirements

- Python 3.8 or higher
- FFmpeg (for video/audio conversions)
- LibreOffice (for office document conversions)

## Installation of Additional Dependencies

### FFmpeg
- Windows: Download from https://ffmpeg.org/download.html
- MacOS: `brew install ffmpeg`
- Linux: `sudo apt-get install ffmpeg`

### LibreOffice
- Windows: Download from https://www.libreoffice.org/download/
- MacOS: `brew install libreoffice`
- Linux: `sudo apt-get install libreoffice`

## Project Structure

```
file-converter/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   └── index.html     # Main page template
├── converters/         # Conversion modules
│   ├── __init__.py
│   ├── pdf_converter.py
│   ├── docx_converter.py
│   └── ...
└── uploads/           # Temporary storage for uploaded files
```

## Troubleshooting

Common issues and solutions:

1. **File not converting**
   - Check if the file format is supported
   - Ensure the file size is under 16MB
   - Verify all dependencies are installed correctly

2. **Application not starting**
   - Make sure the virtual environment is activated
   - Check if all dependencies are installed
   - Verify Python version is 3.8 or higher

3. **Conversion errors**
   - Check if FFmpeg is installed (for media files)
   - Verify LibreOffice is installed (for office documents)
   - Ensure you have write permissions in the uploads directory

## Contributing

Feel free to submit issues and enhancement requests! 

## License

This project is licensed under the MIT License - see the LICENSE file for details. 