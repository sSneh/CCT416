import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Load the preprocessed data from a CSV file
data = pd.read_csv('inputs/Cleaned_Step2.csv')

# Create a new column to store the labels
data['label'] = ''

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()


score_totals = {'positive': 0, 'negative':0, 'neutral': 0}

# Define a labeling function that uses VADER sentiment analysis
def label_tweet(tweet, OG_Tweet):
    # Use VADER sentiment analyzer to classify the tweet as positive, negative or neutral
    scores = analyzer.polarity_scores(tweet)
    compound_score = scores['compound']

    if compound_score >= 0.05:
        label = 'positive'
    elif compound_score <= -0.05:
        label = 'negative'
    else:
        label = 'neutral'

    score_totals[label] += 1

    return label



# Iterate over each row in the DataFrame and assign a label to each tweet
for index, row in data.iterrows():
    tweet = row['cleaned_tweet']
    OG_tweet = row['Tweet']
    label = label_tweet(tweet, OG_tweet)
    data.at[index, 'label'] = label

print(score_totals)

# Save the labeled data to a new CSV file
data.to_csv('inputs/Cleaned_Labeled.csv', index=False)



