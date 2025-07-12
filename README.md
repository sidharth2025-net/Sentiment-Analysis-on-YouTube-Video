

# 📊 YouTube Comment Sentiment Analysis with Gemini

This project provides a comprehensive solution for analyzing the **sentiment of YouTube video comments** using Python, the **YouTube Data API v3**, and **VADER Sentiment Analysis**. It allows users to gain insights into how audiences feel about a video, with visualizations for clarity.

---

## ✨ Features

- **🔗 Comment Fetching**: Download comments from any public YouTube video using its URL.
- **🙅‍♂️ Uploader Comment Exclusion**: Automatically filters out comments made by the video uploader.
- **🧹 Robust Comment Cleaning**:
  - Converts to lowercase
  - Removes leading/trailing whitespace
  - Filters hyperlinks
  - Excludes emoji-only comments
- **🧠 VADER Sentiment Analysis**: Classifies each comment as **Positive**, **Negative**, or **Neutral**.
- **📈 Sentiment Metrics**: Calculates average sentiment scores.
- **💬 Comment Highlights**: Identifies and displays the **most positive** and **most negative** comments.
- **📊 Visualizations**: Bar and Pie charts for sentiment distribution using `matplotlib`.

---

## 🔧 Installation

Clone this repository:

```bash
git clone https://github.com/sidharth2025-net/Sentiment-Analysis-on-YouTube-Video.git
cd Sentiment-Analysis-on-YouTube-Video
