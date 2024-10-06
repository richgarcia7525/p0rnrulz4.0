from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)

# Load the cleaned data
df = pd.read_csv('data/cleaned_xvideos_data.csv')



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/videos')
def get_videos():
    # Limit the number of videos returned, for example, to 20
    videos_data = df.head(20).to_dict(orient='records')
    return jsonify(videos_data)

if __name__ == "__main__":
    app.run(debug=True)











