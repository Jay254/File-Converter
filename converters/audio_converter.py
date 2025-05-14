import os
import ffmpeg

def convert_audio(filepath, target_format):
    """
    Convert audio between different formats using ffmpeg
    """
    output_path = os.path.splitext(filepath)[0] + f'.{target_format}'
    
    try:
        if target_format in ['mp3', 'wav', 'flac', 'aac', 'ogg']:
            # Convert between audio formats
            stream = ffmpeg.input(filepath)
            
            # Set appropriate codec based on target format
            if target_format == 'mp3':
                stream = ffmpeg.output(stream, output_path, acodec='libmp3lame')
            elif target_format == 'wav':
                stream = ffmpeg.output(stream, output_path, acodec='pcm_s16le')
            elif target_format == 'flac':
                stream = ffmpeg.output(stream, output_path, acodec='flac')
            elif target_format == 'aac':
                stream = ffmpeg.output(stream, output_path, acodec='aac')
            elif target_format == 'ogg':
                stream = ffmpeg.output(stream, output_path, acodec='libvorbis')
                
            ffmpeg.run(stream, overwrite_output=True)
        else:
            raise ValueError(f"Conversion from audio to {target_format} is not supported")
            
        return output_path
        
    except ffmpeg.Error as e:
        raise Exception(f"Error converting audio: {str(e)}") 