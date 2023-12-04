from pytube import YouTube
from moviepy.editor import VideoFileClip
import os
import requests

def download_video(url, output_path='downloads_videos'):
    try:
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()
        video.download(output_path)
        print(f"Vídeo baixado com sucesso em: {os.path.join(output_path, video.default_filename)}")
        return os.path.join(output_path, video.default_filename)
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")
        return None

def convert_to_audio(video_path, audio_output_file='output_audio.mp3'):
    try:
        audio_dir = 'audios'
        if not os.path.exists(audio_dir):
            os.makedirs(audio_dir)

        video_clip = VideoFileClip(video_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(os.path.join(audio_dir, audio_output_file))
        print(f"Áudio convertido com sucesso: {os.path.join(audio_dir, audio_output_file)}")
    except Exception as e:
        print(f"Erro ao converter para áudio: {e}")

if __name__ == "__main__":
    video_url = input("Insira a URL do vídeo: ")

    if requests.get(video_url).status_code == 200:
        print("O servidor está disponível.")
        downloaded_video_path = download_video(video_url)
        if downloaded_video_path:
            file_name = os.path.basename(downloaded_video_path).split(".")[0]

        convert_to_audio(downloaded_video_path, file_name + ".mp3")

    else:
        print("O servidor está indisponível.")
