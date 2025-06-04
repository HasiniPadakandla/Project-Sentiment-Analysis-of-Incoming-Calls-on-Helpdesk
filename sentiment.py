from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def get_sentiment(text): 
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)

    if score['compound'] >= 0.05:
        return "Positive", "😊", score['compound']
    elif score['compound'] <= -0.05:
        return "Negative", "😡", score['compound']
    else:
        return "Neutral", "😐", score['compound']

if __name__ == "__main__":
    sample_text = "I am very happy with the service!"
    sentiment, emoji, score = get_sentiment(sample_text)
    print(f"Text: {sample_text}\nSentiment: {sentiment} {emoji}\nScore: {score:.2f}")

