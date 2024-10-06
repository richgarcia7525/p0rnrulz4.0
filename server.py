import pandas as pd
from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Load the cleaned CSV file
df = pd.read_csv('data/cleaned_xvideos_data.csv')  # Make sure this path matches your file structure

@app.route('/')
def index():
    # Prepare trending, newest, most viewed videos
    trending_videos = df.head(3).to_dict(orient='records')
    newest_videos = df.sample(3).to_dict(orient='records')
    most_viewed_videos = df.tail(3).to_dict(orient='records')
    
    return render_template('index.html', trending_videos=trending_videos, newest_videos=newest_videos, most_viewed_videos=most_viewed_videos)

@app.route('/videos')
def videos():
    # Return all videos in JSON format for dynamic loading
    return jsonify(df.to_dict(orient='records'))

# New route examples for specific categories
@app.route('/straight_videos')
def straight_videos():
    # Filtering based on tags or categories if relevant
    straight_videos_df = df[df['Tags'].str.contains('straight', case=False, na=False)]
    straight_videos = straight_videos_df.to_dict(orient='records')
    return render_template('category.html', category_name='Straight Videos', videos=straight_videos)

@app.route('/gay_videos')
def gay_videos():
    # Filtering for gay videos
    gay_videos_df = df[df['Tags'].str.contains('gay', case=False, na=False)]
    gay_videos = gay_videos_df.to_dict(orient='records')
    return render_template('category.html', category_name='Gay Videos', videos=gay_videos)

@app.route('/trans_videos')
def trans_videos():
    # Filtering for trans videos
    trans_videos_df = df[df['Tags'].str.contains('trans', case=False, na=False)]
    trans_videos = trans_videos_df.to_dict(orient='records')
    return render_template('category.html', category_name='Trans Videos', videos=trans_videos)

@app.route('/trending_videos')
def trending_videos():
    trending_videos_data = df.head(10).to_dict(orient='records')  # Adjust the filter as needed
    return render_template('category.html', category_name='Trending Videos', videos=trending_videos_data)

@app.route('/newest_videos')
def newest_videos():
    newest_videos_data = df.sample(10).to_dict(orient='records')  # You can change this filter to select the newest videos in some way.
    return render_template('category.html', category_name='Newest Videos', videos=newest_videos_data)

@app.route('/most_viewed_videos')
def most_viewed_videos():
    most_viewed_videos_data = df.nlargest(10, 'Views').to_dict(orient='records')  # Adjust the filter to select most viewed videos if there is a column for views.
    return render_template('category.html', category_name='Most Viewed Videos', videos=most_viewed_videos_data)


if __name__ == '__main__':
    app.run(debug=True)













