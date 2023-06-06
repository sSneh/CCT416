import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Load the preprocessed data from a CSV file
data = pd.read_csv('Sandbox_Step2.csv')

# Create a new column to store the labels
data['label'] = ''

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()


# Define a labeling function that uses VADER sentiment analysis
def label_tweet(tweet):
    # Use VADER sentiment analyzer to classify the tweet as positive, negative or neutral
    scores = analyzer.polarity_scores(tweet)
    compound_score = scores['compound']
    if compound_score >= 0.05:
        label = 'positive'
    elif compound_score <= -0.05:
        label = 'negative'
    else:
        label = 'neutral'
    return label


# Iterate over each row in the DataFrame and assign a label to each tweet
for index, row in data.iterrows():
    tweet = row['cleaned_tweet']
    label = label_tweet(tweet)
    data.at[index, 'label'] = label

# Save the labeled data to a new CSV file
data.to_csv('Sandbox_labeled.csv', index=False)

