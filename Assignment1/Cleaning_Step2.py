import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import matplotlib.pyplot as plt
from collections import Counter
from bs4 import BeautifulSoup
import re

# load the csv file into a pandas dataframe
df = pd.read_csv("inputs/Cleaned_Step1.csv")

# initialize the NLTK lemmatizer and stopwords
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))
stop_exclusions = {"while", 'but', "shouldn't", 'against', 'nor', 'more', 'because', 'very', "don't", "isn't", 'doesn', 'down', 'no', "couldn't", 'should', 'won', 'most', "weren't", 'not', "aren't", "doesn't", "wouldn't", "won't"}
stop_words = stop_words - stop_exclusions
#print(stop_words)

# define a function to clean each tweet
def clean_tweet(tweet):
    # Remove single letters but avoid (ai, ip)
    tweet = re.sub(r"(?!(a\.|i\.|A\.|I\.))\b\w\b", "", tweet)
    #tweet = re.sub(r"(?!\b(ai|ip|a\.i)\b)\b\w{2}\b", "", tweet.lower())

    # Remove two or more dots "..."
    tweet = re.sub(r"\.{2,}", "", tweet)

    # Remove "" "
    tweet = re.sub(r"\"{1,}", "", tweet)

    # Remove amp (residue of &)
    tweet = re.sub(r'\b(amp)\b', "", tweet)

    # tokenize the tweet
    tokens = word_tokenize(tweet)

    # remove digits and punctuation
    tokens = [
        token
        for token in tokens
        if not token.isdigit() and (token not in string.punctuation or token in '?!')
    ]

    # remove stop words
    tokens = [token for token in tokens if token.lower() not in stop_words]

    # lemmatize the tokens
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    #print(tokens)

    # join the tokens back into a string
    cleaned_tweet = " ".join(tokens)

    return cleaned_tweet


# apply the clean_tweet function to each tweet in the dataframe
df["cleaned_tweet"] = df["Tweet"].apply(clean_tweet)

# save the cleaned tweets to a new CSV file
df.to_csv("inputs/Cleaned_Step2.csv", index=False)

# load the cleaned tweets CSV file into a pandas dataframe
df = pd.read_csv("inputs/Cleaned_Step2.csv")

# count the frequency of each word
word_freq = Counter()
for tweet in df["cleaned_tweet"]:
    word_list = tweet.split()
    word_list = [word for word in word_list if word not in "?!"]
    word_freq.update(word_list)

# get the top 10 most frequent words and their counts
top_words = word_freq.most_common(10)
top_words_list = [word[0] for word in top_words]
top_words_counts = [word[1] for word in top_words]

# print(top_words)

# plot the top 10 most frequent words on a bar graph
plt.bar(top_words_list, top_words_counts)
plt.title("Top 10 Most Frequent Words")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.show()
