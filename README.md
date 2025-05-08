# File Converter

A web-based file converter that supports conversion between the top 10 most common file formats.

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

## Contributing

Feel free to submit issues and enhancement requests! 