!pip install vaderSentiment
import re
import emoji
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googleapiclient.discovery import build

# Replace with your YouTube API Key
API_KEY = 'AIzaSyA9vUH2MnTmHGwfwcEOhg_iLNUnv5t8MIM'

# Function to extract video ID from full YouTube URL
def extract_video_id(url):
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
    return match.group(1) if match else None

# Function to fetch YouTube comments
def get_youtube_comments(video_id):
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    # Fetch video details to get the uploader's channel ID
    video_response = youtube.videos().list(part='snippet', id=video_id).execute()
    uploader_channel_id = video_response['items'][0]['snippet']['channelId']

    print(f"Fetching comments for Video ID: {video_id}...")

    comments = []
    next_page_token = None

    while True:
        request = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            maxResults=100,
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response.get('items', []):
            comment_data = item['snippet']['topLevelComment']['snippet']
            if comment_data['authorChannelId']['value'] != uploader_channel_id:
                comments.append(comment_data['textDisplay'])

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    print(f"Total comments fetched: {len(comments)}")
    return comments

# Function to clean and filter comments
def clean_comments(comments):
    hyperlink_pattern = re.compile(r"http[s]?://\S+")
    threshold_ratio = 0.65
    relevant_comments = []

    for comment in comments:
        comment = comment.lower().strip()
        emoji_count = emoji.emoji_count(comment)
        text_characters = len(re.sub(r'\s', '', comment))

        # Check if the comment contains alphanumeric characters and is not a hyperlink
        if any(char.isalnum() for char in comment) and not hyperlink_pattern.search(comment):
            # Ensure a reasonable emoji-to-text ratio
            if emoji_count == 0 or (text_characters / (text_characters + emoji_count)) > threshold_ratio:
                relevant_comments.append(comment)

    print(f"Filtered relevant comments: {len(relevant_comments)}")
    return relevant_comments

# Function to analyze sentiment using VADER
def analyze_sentiments(comments):
    analyzer = SentimentIntensityAnalyzer()
    polarity_scores = []
    positive_comments, negative_comments, neutral_comments = [], [], []

    for comment in comments:
        score = analyzer.polarity_scores(comment)['compound']
        polarity_scores.append(score)

        if score > 0.05:
            positive_comments.append(comment)
        elif score < -0.05:
            negative_comments.append(comment)
        else:
            neutral_comments.append(comment)

    return polarity_scores, positive_comments, negative_comments, neutral_comments

# Function to visualize sentiment analysis results
def visualize_results(positive, negative, neutral):
    labels = ['Positive', 'Negative', 'Neutral']
    comment_counts = [len(positive), len(negative), len(neutral)]

    # Bar chart
    plt.bar(labels, comment_counts, color=['green', 'red', '#9AD8D8'])
    plt.xlabel('Sentiment')
    plt.ylabel('Comment Count')
    plt.title('Sentiment Analysis of Comments')
    plt.show()

    # Pie chart
    plt.figure(figsize=(10, 6))
    plt.pie(comment_counts, labels=labels, autopct='%1.1f%%', colors=['green', 'red', '#9AD8D8'])
    plt.title('Sentiment Distribution')
    plt.show()

# Main execution
if __name__ == "__main__":
    video_url = input("Enter YouTube Video URL: ")
    video_id = extract_video_id(video_url)

    if not video_id:
        print("Invalid YouTube URL. Please enter a valid link.")
    else:
        comments = get_youtube_comments(video_id)
        cleaned_comments = clean_comments(comments)

        if cleaned_comments:
            polarity_scores, pos_comments, neg_comments, neu_comments = analyze_sentiments(cleaned_comments)

            avg_polarity = sum(polarity_scores) / len(polarity_scores)
            print(f"\nAverage Sentiment Score: {avg_polarity:.2f}")

            if avg_polarity > 0.05:
                print("Overall Sentiment: Positive")
            elif avg_polarity < -0.05:
                print("Overall Sentiment: Negative")
            else:
                print("Overall Sentiment: Neutral")

            if polarity_scores:
                most_positive_index = polarity_scores.index(max(polarity_scores))
                most_negative_index = polarity_scores.index(min(polarity_scores))

                if pos_comments:
                    print("\nMost Positive Comment:")
                    print(cleaned_comments[most_positive_index])
                else:
                    print("\nNo positive comments found.")

                if neg_comments:
                    print("\nMost Negative Comment:")
                    print(cleaned_comments[most_negative_index])
                else:
                    print("\nNo negative comments found.")

            # Generate visualizations
            visualize_results(pos_comments, neg_comments, neu_comments)
        else:
            print("No relevant comments found for sentiment analysis.")
