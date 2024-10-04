from flask import Flask, render_template
import json

app = Flask(__name__)

def load_videos():
    # Make sure the file path and JSON structure are correct
    with open('videos.json', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    # Load the videos before passing to the template
    try:
        videos = load_videos()
    except FileNotFoundError:
        videos = []

    return render_template('index.html', videos=videos)

if __name__ == '__main__':
    app.run(debug=True)




