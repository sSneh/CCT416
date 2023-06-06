import csv
import nltk
from nltk.corpus import sentiwordnet as swn
import matplotlib.pyplot as plt

# Open the CSV file and read in the cleaned texts
with open('inputs/Cleaned_Step2.csv', 'r') as file:
    reader = csv.reader(file)
    tweets = [row[6] for row in reader]

# Define a function to calculate the sentiment scores
def get_sentiment_scores(tweet):
    # Tokenize the tweet into words
    words = nltk.word_tokenize(tweet)
    # Calculate the sentiment scores for each word using SentiWordNet
    pos_score, neg_score, obj_score = 0, 0, 0
    for word in words:
        synsets = list(swn.senti_synsets(word))
        if len(synsets) > 0:
            synset = synsets[0]
            pos_score += synset.pos_score()
            neg_score += synset.neg_score()
            obj_score += synset.obj_score()
    # Calculate the overall sentiment score
    if pos_score > neg_score:
        sentiment = 'Positive'
        score = pos_score
    elif pos_score < neg_score:
        sentiment = 'Negative'
        score = neg_score
    else:
        sentiment = 'Neutral'
        score = obj_score
    return sentiment, score


# Calculate the sentiment scores for each tweet
sentiment_scores = [get_sentiment_scores(tweet) for tweet in tweets]

# Count the number of positive, negative, and neutral tweets
positive_count = len([score for score in sentiment_scores if score[0] == 'Positive'])
negative_count = len([score for score in sentiment_scores if score[0] == 'Negative'])
neutral_count = len([score for score in sentiment_scores if score[0] == 'Neutral'])

# Print out the relevant scores
print('Overall Sentiment Analysis')
print('----------------------------')
print(f'Positive: {positive_count} ({positive_count / len(tweets) * 100:.2f}%)')
print(f'Negative: {negative_count} ({negative_count / len(tweets) * 100:.2f}%)')
print(f'Neutral: {neutral_count} ({neutral_count / len(tweets) * 100:.2f}%)')

# Plot the sentiment counts in a bar graph
labels = ['Positive', 'Negative', 'Neutral']
values = [positive_count, negative_count, neutral_count]
plt.bar(labels, values)
plt.title('Sentiment Analysis (SentiWord)')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()

# Calculate the polarity of the sentiments
polarity_scores = [2 * score[1] - 1 for score in sentiment_scores]

# Plot the scatter plot of polarity
plt.figure()
plt.scatter(range(len(polarity_scores)), polarity_scores, color='green')
plt.title('Polarity')
plt.xlabel('Tweet')
plt.ylabel('Polarity')
plt.ylim(-1, 1)  # Set the y-axis limits to -1 and 1
plt.show()
