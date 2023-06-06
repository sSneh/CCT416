import csv
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

# Initialize the sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Open the CSV file and read the tweets
with open('SG3B_Step2.csv', 'r') as file:
    reader = csv.DictReader(file)
    positive_count = 0
    negative_count = 0
    neutral_count = 0
    pos_score_total = 0
    neg_score_total = 0
    neu_score_total = 0
    polarities = []  # List to store the polarity scores for scatter plot

    for row in reader:
        tweet = row['cleaned_tweet']

        # Use the VADER sentiment analyzer to compute the sentiment score
        score = analyzer.polarity_scores(tweet)['compound']

        # Categorize the sentiment score as positive, negative, or neutral
        if score > 0:
            positive_count += 1
        elif score < 0:
            negative_count += 1
        else:
            neutral_count += 1

        # Add the VADER scores to the total for computing the average later
        pos_score_total += analyzer.polarity_scores(tweet)['pos']
        neg_score_total += analyzer.polarity_scores(tweet)['neg']
        neu_score_total += analyzer.polarity_scores(tweet)['neu']

        # Store the polarity score for scatter plot
        polarities.append(score)

    # Compute the average VADER scores
    total_count = positive_count + negative_count + neutral_count
    if total_count > 0:
        pos_score_avg = pos_score_total / total_count
        neg_score_avg = neg_score_total / total_count
        neu_score_avg = neu_score_total / total_count
    else:
        pos_score_avg = neg_score_avg = neu_score_avg = 0.0

    # Plot the sentiment summary as a bar chart
    labels = ['Positive', 'Negative', 'Neutral']
    counts = [positive_count, negative_count, neutral_count]
    plt.bar(labels, counts)
    plt.xlabel('Sentiment')
    plt.ylabel('Number of tweets')
    plt.show()  # Display the chart

    # Plot the polarity scatter plot
    plt.scatter(range(len(polarities)), polarities, c=polarities, cmap='coolwarm')
    plt.xlabel('Tweet')
    plt.ylabel('Polarity Score')
    plt.colorbar(label='Polarity')
    plt.show()  # Display the scatter plot

    # Write the sentiment summary and VADER statistics to a new CSV file
    with open('sentiment_summaryufo.csv', 'w', newline='') as output_file:
        writer = csv.writer(output_file)

        writer.writerow(['Sentiment', 'Count'])
        writer.writerow(['Positive', positive_count])
        writer.writerow(['Negative', negative_count])
        writer.writerow(['Neutral', neutral_count])

        writer.writerow([])  # Add a blank line between sections

        writer.writerow(['VADER Statistic', 'Value'])
        writer.writerow(['Positive Score (avg)', pos_score_avg])
        writer.writerow(['Negative Score (avg)', neg_score_avg])
        writer.writerow(['Neutral Score (avg)', neu_score_avg])


# Print the sentiment counts
print('Sentiment Counts:')
print('Positive:', positive_count)
print('Negative:', negative_count)
print('Neutral:', neutral_count)
