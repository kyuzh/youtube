from flask import Flask, render_template, request
from pytube import YouTube
import os

app = Flask(__name__)

def download_video(url, output_path='.'):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(output_path)
        return True, yt.title
    except Exception as e:
        return False, str(e)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        video_url = request.form['video_url']
        output_path = request.form.get('output_path', 'downloads')  # Utilisez 'downloads' par défaut si le champ est vide
        success, title = download_video(video_url, output_path)
        if success:
            message = f'Téléchargement réussi: {title}'
        else:
            message = f'Erreur lors du téléchargement: {title}'
        return render_template('index.html', message=message)
    return render_template('index.html', message='Bienvenue sur mon site web!')

if __name__ == '__main__':
    app.run(debug=True)