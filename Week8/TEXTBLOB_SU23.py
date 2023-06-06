#SUMMER 2023 TEXTBLOB CODE

import csv
from textblob import TextBlob
import matplotlib.pyplot as plt

# Open the CSV file containing tweets
with open('SG3B_Step2.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')

    # Initialize variables to keep track of sentiment counts
    positive_count = 0
    negative_count = 0
    neutral_count = 0

    # Initialize lists to store polarity and subjectivity values
    polarity_values = []
    subjectivity_values = []

    # Loop through each row in the CSV file
    for row in reader:
        tweet = row[6]
        # Create a TextBlob object for each tweet
        blob = TextBlob(tweet)
        # Get the sentiment polarity of the tweet (ranging from -1 to 1)
        sentiment_polarity = blob.sentiment.polarity
        # Get the sentiment subjectivity of the tweet (ranging from 0 to 1)
        sentiment_subjectivity = blob.sentiment.subjectivity

        # Classify sentiment as positive, negative, or neutral
        if sentiment_polarity > 0:
            sentiment_class = 'Positive'
            positive_count += 1
        elif sentiment_polarity < 0:
            sentiment_class = 'Negative'
            negative_count += 1
        else:
            sentiment_class = 'Neutral'
            neutral_count += 1

        # Append polarity and subjectivity values to the respective lists
        polarity_values.append(sentiment_polarity)
        subjectivity_values.append(sentiment_subjectivity)

    # Plot a bar chart of the overall sentiment
    labels = ['Positive', 'Negative', 'Neutral']
    counts = [positive_count, negative_count, neutral_count]
    colors = 'blue'
    plt.subplot(1, 2, 1)
    plt.bar(labels, counts, color=colors)
    plt.title('Sentiment Analysis (TextBlob)')
    plt.xlabel('Sentiment Class')
    plt.ylabel('Count')

    # Plot a scatter plot of polarity
    plt.figure()
    plt.scatter(range(len(polarity_values)), polarity_values, color='green')
    plt.title('Polarity')
    plt.xlabel('Tweet')
    plt.ylabel('Polarity')

    # Plot a scatter plot of subjectivity
    plt.figure()
    plt.scatter(range(len(subjectivity_values)), subjectivity_values, color='red')
    plt.title('Subjectivity')
    plt.xlabel('Tweet')
    plt.ylabel('Subjectivity')

    # Display the plots
    plt.show()

    # Print overall sentiment scores
    print("Positive score:", positive_count)
    print("Negative score:", negative_count)
    print("Neutral score:", neutral_count)
