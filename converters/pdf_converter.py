import os
from PyPDF2 import PdfReader, PdfWriter
from pdf2docx import Converter
from reportlab.pdfgen import canvas
from PIL import Image
import img2pdf

def convert_pdf(filepath, target_format):
    """
    Convert PDF to various formats
    """
    output_path = os.path.splitext(filepath)[0] + f'.{target_format}'
    
    if target_format == 'docx':
        # PDF to DOCX conversion
        cv = Converter(filepath)
        cv.convert(output_path)
        cv.close()
        
    elif target_format == 'txt':
        # PDF to TXT conversion
        reader = PdfReader(filepath)
        with open(output_path, 'w', encoding='utf-8') as f:
            for page in reader.pages:
                f.write(page.extract_text())
                
    elif target_format in ['jpg', 'png']:
        # PDF to Image conversion
        reader = PdfReader(filepath)
        page = reader.pages[0]  # Convert first page only
        image = page.extract_image()
        if image:
            img = Image.open(image)
            img.save(output_path)
            
    else:
        raise ValueError(f"Conversion from PDF to {target_format} is not supported")
        
    return output_path 