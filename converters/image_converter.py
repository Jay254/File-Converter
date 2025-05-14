import os
from PIL import Image
import img2pdf

def convert_image(filepath, target_format):
    """
    Convert images between different formats
    """
    output_path = os.path.splitext(filepath)[0] + f'.{target_format}'
    
    if target_format in ['jpg', 'jpeg', 'png', 'bmp', 'gif', 'webp']:
        # Convert between image formats
        img = Image.open(filepath)
        if target_format == 'jpg' or target_format == 'jpeg':
            # Convert to RGB if converting to JPG
            if img.mode in ('RGBA', 'LA'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[-1])
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
        img.save(output_path)
        
    elif target_format == 'pdf':
        # Convert image to PDF
        with open(output_path, "wb") as f:
            f.write(img2pdf.convert(filepath))
            
    else:
        raise ValueError(f"Conversion from image to {target_format} is not supported")
        
    return output_path 