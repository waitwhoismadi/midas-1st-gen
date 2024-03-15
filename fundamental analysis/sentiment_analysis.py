import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyze_sentiment(article):
    sid = SentimentIntensityAnalyzer()

    sentiment_score = sid.polarity_scores(article)

    if sentiment_score['compound'] >= 0.05:
        sentiment_label = 'Positive'
    elif sentiment_score['compound'] <= -0.05:
        sentiment_label = 'Negative'
    else:
        sentiment_label = 'Neutral'

    return sentiment_label

article = """
Bitcoin (BTC) climbed past $47,000 Friday as U.S.-based spot bitcoin exchange-traded funds (ETFs) booked one of their largest net inflows Thursday since their debut.
The largest crypto by market capitalization ran to as high as $47,699, the highest since the bitcoin ETF launch day, before it buckled to $46,700 in a swift sell-off. Soon after, prices quickly rebounded slightly over $47,000. At press time, BTC was up 4.5% over the past 24 hours, outperforming the CoinDesk 20 Index (CD20), a measure of the biggest cryptocurrencies, which advanced 3.8%.
The price surge happened as spot ETFs increased their net bitcoin holdings by 9,260 BTC, according to CoinDesk calculation based on the issuers' website. That translated to over $400 million in inflows, according to BitMex Research data, the highest figure since January 17.
"""
sentiment = analyze_sentiment(article)
print("Sentiment:", sentiment)
