import os
import ffmpeg

def convert_video(filepath, target_format):
    """
    Convert videos between different formats using ffmpeg
    """
    output_path = os.path.splitext(filepath)[0] + f'.{target_format}'
    
    try:
        if target_format in ['mp4', 'avi', 'mov', 'mkv']:
            # Convert between video formats
            stream = ffmpeg.input(filepath)
            stream = ffmpeg.output(stream, output_path)
            ffmpeg.run(stream, overwrite_output=True)
            
        elif target_format == 'mp3':
            # Extract audio from video
            stream = ffmpeg.input(filepath)
            stream = ffmpeg.output(stream, output_path, acodec='libmp3lame')
            ffmpeg.run(stream, overwrite_output=True)
            
        elif target_format == 'gif':
            # Convert video to GIF
            stream = ffmpeg.input(filepath)
            stream = ffmpeg.output(stream, output_path, vf='fps=10,scale=320:-1:flags=lanczos')
            ffmpeg.run(stream, overwrite_output=True)
            
        else:
            raise ValueError(f"Conversion from video to {target_format} is not supported")
            
        return output_path
        
    except ffmpeg.Error as e:
        raise Exception(f"Error converting video: {str(e)}") 