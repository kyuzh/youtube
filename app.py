# app.py

from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)


def download_video(url, output_path='.'):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(output_path)
        return True, f'Téléchargement réussi: {yt.title}'
    except Exception as e:
        return False, f'Erreur lors du téléchargement: {str(e)}'


@app.route('/', methods=['GET', 'POST'])
def home():
    message = "Télécharger video youtube avec url"

    if request.method == 'POST':
        video_url = request.form['video_url']
        output_path = request.form.get('output_path', 'downloads')
        success, message = download_video(video_url, output_path)

    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True, port=8001)