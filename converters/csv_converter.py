import os
import pandas as pd
from openpyxl import Workbook
from docx import Document
import json

def convert_csv(filepath, target_format):
    """
    Convert CSV files to various formats
    """
    output_path = os.path.splitext(filepath)[0] + f'.{target_format}'
    
    if target_format == 'xlsx':
        # CSV to Excel conversion
        df = pd.read_csv(filepath)
        df.to_excel(output_path, index=False)
        
    elif target_format == 'html':
        # CSV to HTML conversion
        df = pd.read_csv(filepath)
        html_content = df.to_html(index=False)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
    elif target_format == 'json':
        # CSV to JSON conversion
        df = pd.read_csv(filepath)
        df.to_json(output_path, orient='records', indent=2)
        
    elif target_format == 'docx':
        # CSV to DOCX conversion
        df = pd.read_csv(filepath)
        doc = Document()
        
        # Add table
        table = doc.add_table(rows=1, cols=len(df.columns))
        table.style = 'Table Grid'
        
        # Add headers
        header_cells = table.rows[0].cells
        for i, column in enumerate(df.columns):
            header_cells[i].text = column
            
        # Add data
        for _, row in df.iterrows():
            cells = table.add_row().cells
            for i, value in enumerate(row):
                cells[i].text = str(value)
                
        doc.save(output_path)
        
    else:
        raise ValueError(f"Conversion from CSV to {target_format} is not supported")
        
    return output_path 