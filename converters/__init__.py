from .pdf_converter import convert_pdf
from .docx_converter import convert_docx
from .image_converter import convert_image
from .video_converter import convert_video
from .audio_converter import convert_audio
from .excel_converter import convert_excel
from .powerpoint_converter import convert_powerpoint
from .text_converter import convert_text
from .html_converter import convert_html
from .csv_converter import convert_csv

def get_converter(source_format, target_format):
    converters = {
        'pdf': convert_pdf,
        'docx': convert_docx,
        'jpg': convert_image,
        'jpeg': convert_image,
        'png': convert_image,
        'mp4': convert_video,
        'mp3': convert_audio,
        'xlsx': convert_excel,
        'pptx': convert_powerpoint,
        'txt': convert_text,
        'html': convert_html,
        'csv': convert_csv
    }
    
    return converters.get(source_format) 