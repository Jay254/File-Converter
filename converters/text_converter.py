import os
from reportlab.pdfgen import canvas
from docx import Document
import markdown

def convert_text(filepath, target_format):
    """
    Convert text files to various formats
    """
    output_path = os.path.splitext(filepath)[0] + f'.{target_format}'
    
    if target_format == 'pdf':
        # Text to PDF conversion
        c = canvas.Canvas(output_path)
        with open(filepath, 'r', encoding='utf-8') as f:
            y = 750  # Starting y position
            for line in f:
                c.drawString(50, y, line.strip())
                y -= 12  # Move down for next line
                if y < 50:  # Start new page if we're at the bottom
                    c.showPage()
                    y = 750
        c.save()
        
    elif target_format == 'docx':
        # Text to DOCX conversion
        doc = Document()
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                doc.add_paragraph(line.strip())
        doc.save(output_path)
        
    elif target_format == 'html':
        # Text to HTML conversion
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        html_content = ['<html><body>']
        for line in content.split('\n'):
            html_content.append(f'<p>{line}</p>')
        html_content.append('</body></html>')
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(html_content))
            
    else:
        raise ValueError(f"Conversion from text to {target_format} is not supported")
        
    return output_path 