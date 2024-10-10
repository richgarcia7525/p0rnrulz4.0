import pandas as pd
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# Load the cleaned CSV file
df = pd.read_csv('data/cleaned_xvideos_data.csv')

# Route for handling categories and sections dynamically (with pagination)
@app.route('/category/<category_name>/<section>/<int:page>', methods=['GET'])
def category_page(category_name, section, page=1):
    # Items per page
    per_page = 5

    # Filter videos based on category name (straight, gay, trans, etc.)
    category_videos = df[df['Tags'].str.contains(category_name, case=False, na=False)]

    # Further filter based on section (newest, most viewed, trending)
    if section == 'newest':
        section_videos = category_videos.sample(frac=1)  # Shuffle for newest
    elif section == 'most_viewed':
        section_videos = category_videos.nlargest(len(category_videos), 'Duration')  # Using 'Duration' as a proxy for views
    elif section == 'trending':
        section_videos = category_videos.head(len(category_videos))
    else:
        section_videos = category_videos.head(len(category_videos))  # Default

    # Implement pagination logic
    total_videos = len(section_videos)
    total_pages = (total_videos + per_page - 1) // per_page  # Calculate total pages
    section_videos = section_videos.iloc[(page - 1) * per_page: page * per_page]

    return render_template('videos.html', category_name=category_name.title(), section=section, videos=section_videos.to_dict(orient='records'), page=page, total_pages=total_pages)

# Route for the home page
@app.route('/')
def index():
    trending_videos = df.head(3).to_dict(orient='records')
    newest_videos = df.sample(3).to_dict(orient='records')
    most_viewed_videos = df.nlargest(3, 'Duration').to_dict(orient='records')
    straight_videos = df[df['Tags'].str.contains('straight')].head(3).to_dict(orient='records')
    gay_videos = df[df['Tags'].str.contains('gay')].head(3).to_dict(orient='records')
    trans_videos = df[df['Tags'].str.contains('trans')].head(3).to_dict(orient='records')

    return render_template('index.html', trending_videos=trending_videos, newest_videos=newest_videos, most_viewed_videos=most_viewed_videos, straight_videos=straight_videos, gay_videos=gay_videos, trans_videos=trans_videos)


# API route to return paginated videos as JSON
@app.route('/videos')
def videos():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))  # Default to 10 items per page
    limit = min(limit, 20)  # Set a hard max limit of 20 items per page
    offset = (page - 1) * limit

    video_data = df.iloc[offset:offset + limit].to_dict(orient='records')
    
    if not video_data:
        return jsonify({'error': 'No more videos'}), 404

    return jsonify(video_data)

if __name__ == '__main__':
    app.run(debug=True)















