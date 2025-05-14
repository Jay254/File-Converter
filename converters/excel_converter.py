import os
import pandas as pd
from openpyxl import load_workbook
import comtypes.client
import pythoncom

def convert_excel(filepath, target_format):
    """
    Convert Excel files to various formats
    """
    output_path = os.path.splitext(filepath)[0] + f'.{target_format}'
    
    if target_format == 'csv':
        # Excel to CSV conversion
        df = pd.read_excel(filepath)
        df.to_csv(output_path, index=False)
        
    elif target_format == 'pdf':
        # Excel to PDF conversion
        excel = comtypes.client.CreateObject('Excel.Application')
        excel.Visible = False
        try:
            wb = excel.Workbooks.Open(os.path.abspath(filepath))
            wb.ExportAsFixedFormat(0, os.path.abspath(output_path))
        finally:
            wb.Close()
            excel.Quit()
            
    elif target_format == 'html':
        # Excel to HTML conversion
        df = pd.read_excel(filepath)
        html_content = df.to_html(index=False)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
    else:
        raise ValueError(f"Conversion from Excel to {target_format} is not supported")
        
    return output_path 