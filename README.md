YouTube Comment Sentiment Analysis with Gemini
This project provides a comprehensive solution for analyzing the sentiment of YouTube video comments. It leverages Python and the YouTube Data API v3 to fetch comments, cleans them using regular expressions and emoji handling, and then performs sentiment analysis with the VADER (Valence Aware Dictionary and sentiment Reasoner) lexicon. The results are visualized through intuitive charts, offering insights into the overall sentiment surrounding a video.

Features
Comment Fetching: Downloads comments from any public YouTube video using its URL.

Uploader Comment Exclusion: Automatically filters out comments made by the video's uploader to focus solely on audience sentiment.

Robust Comment Cleaning:

Converts comments to lowercase and removes leading/trailing whitespace.

Filters out comments containing hyperlinks.

Excludes comments that are primarily emojis, ensuring text-based analysis.

VADER Sentiment Analysis: Utilizes the VADER lexicon to classify comments as positive, negative, or neutral.

Sentiment Metrics: Calculates the average sentiment score for all analyzed comments.

Comment Highlights: Identifies and displays the most positive and most negative comments.

Visualizations: Generates a bar chart and a pie chart to visually represent the distribution of positive, negative, and neutral sentiments.

Installation
To get this project up and running, follow these steps:

Clone the repository:

git clone https://github.com/YOUR_USERNAME/youtube-sentiment-analysis.git
cd youtube-sentiment-analysis

(Remember to replace YOUR_USERNAME with your actual GitHub username.)

Install the required Python packages:

pip install vaderSentiment matplotlib google-api-python-client emoji

API Key Setup (Crucial!)
This script requires a YouTube Data API v3 key to access YouTube comments. Here's how to obtain and configure it:

Go to the Google Cloud Console: Visit https://console.cloud.google.com/.

Create a New Project: If you don't have one, create a new project.

Enable the YouTube Data API v3:

In your new or existing project, navigate to "APIs & Services" > "Library".

Search for "YouTube Data API v3" and enable it.

Create API Credentials:

Go to "APIs & Services" > "Credentials".

Click "Create Credentials" > "API key".

Copy the generated API key.

Configure the API Key in the script:

Open the youtube_sentiment_analyzer.py file (or whatever you named the main script).

Find the line API_KEY = 'AIzaSyA9vUH2MnTmHGwfwcEOhg_iLNUnN5t8MIM' (or similar).

Replace the placeholder API key with the API key you generated from the Google Cloud Console.

API_KEY = 'YOUR_YOUTUBE_API_KEY'  # Replace with your actual YouTube API Key

Usage
After setting up your API key, you can run the script:

Execute the Python script:

python youtube_sentiment_analyzer.py

Enter YouTube Video URL:
The script will prompt you to enter the full URL of the YouTube video you wish to analyze.

Enter YouTube Video URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ

View Results:
The script will then:

Fetch and clean the comments.

Perform sentiment analysis.

Print an overall sentiment summary, including the average sentiment score, and the most positive/negative comments.

Display two matplotlib plots: a bar chart and a pie chart illustrating the sentiment distribution.

Example Output
Fetching comments for Video ID: dQw4w9WgXcQ...
Total comments fetched: 500
Filtered relevant comments: 450

Average Sentiment Score: 0.15
Overall Sentiment: Positive

Most Positive Comment:
This video made my day, absolutely brilliant!

Most Negative Comment:
I can't believe how bad this is, total waste of time.

(Followed by the bar and pie charts displayed in separate windows)

Contributing
Contributions are always welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to:

Fork the repository.

Create a new branch (git checkout -b feature/your-feature-name).

Make your changes and commit them (git commit -m 'Add new feature').

Push to your branch (git push origin feature/your-feature-name).

Open a Pull Request against the main branch of this repository.

License
This project is licensed under the MIT License - see the LICENSE file for details.
