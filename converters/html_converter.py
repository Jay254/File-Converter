import os
from bs4 import BeautifulSoup
from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

def convert_html(filepath, target_format):
    """
    Convert HTML files to various formats
    """
    output_path = os.path.splitext(filepath)[0] + f'.{target_format}'
    
    if target_format == 'pdf':
        # HTML to PDF conversion using reportlab
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
        doc = SimpleDocTemplate(output_path, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []
        
        for p in soup.find_all('p'):
            text = p.get_text()
            p = Paragraph(text, styles['Normal'])
            story.append(p)
            
        doc.build(story)
        
    elif target_format == 'docx':
        # HTML to DOCX conversion
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
        doc = Document()
        for p in soup.find_all('p'):
            doc.add_paragraph(p.get_text())
            
        doc.save(output_path)
        
    elif target_format == 'txt':
        # HTML to TXT conversion
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
        with open(output_path, 'w', encoding='utf-8') as f:
            for p in soup.find_all('p'):
                f.write(p.get_text() + '\n')
                
    else:
        raise ValueError(f"Conversion from HTML to {target_format} is not supported")
        
    return output_path 