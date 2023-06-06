import csv
import preprocessor as p
import re
from collections import Counter

# read the csv file
with open("inputs/SG3B.csv", "r", encoding="UTF-8") as file:
    reader = csv.reader(file)
    data = list(reader)

# print the number of original tweets
print("Number of original tweets:", len(data))

# remove the header row
header = data[0]
data = data[1:]

# initialize the cleaned tweets set and list
seen_tweets = set()
cleaned_tweets = []

# iterate through each row of the data
for row in data:
    # extract the tweet
    tweet = row[3]

    p.set_options(p.OPT.URL, p.OPT.MENTION, p.OPT.RESERVED, p.OPT.EMOJI, p.OPT.SMILEY, p.OPT.NUMBER)
   
    # clean the tweet and remove numbers
    cleaned_tweet = re.sub(r'\d+', '', p.clean(tweet))

    # remove hastags 2 in a row
    cleaned_tweet = re.sub(r'(#(\w+) *){2,}', '', cleaned_tweet)

    # remove hastags at the end of a tweet (only after punctuation)
    cleaned_tweet = re.sub(r'[!\"#\$%&\'\(\)\*\+,-\./:;<=>\?@\[\\\]\^_`{\|}~] #(\w+)$', '', cleaned_tweet)

    # remaining hastags should be part of a sentence and are converted to normal words
    cleaned_tweet = cleaned_tweet.replace("#", "")

    if not tweet.startswith("RT "):
        # check if we've seen this tweet before
        if cleaned_tweet not in seen_tweets and "ai" in cleaned_tweet.lower():
            # mark this tweet as seen
            seen_tweets.add(cleaned_tweet)

            # append the cleaned tweet to the cleaned_tweets list
            cleaned_tweets.append(cleaned_tweet)
            #print("->",cleaned_tweet)
        # if re.search(r'(#(\w+) *){1,}', cleaned_tweet) != None:
        #     print("->",cleaned_tweet)

print("Number of Cleaned tweets:", len(cleaned_tweets))

# write the cleaned tweets to a new csv file
with open("inputs/Cleaned_Step1.csv", "w", newline="", encoding="UTF-8") as file:
    writer = csv.writer(file)

    # write the header
    writer.writerow(header)

    # write the cleaned tweets
    for cleaned_tweet in cleaned_tweets:
        writer.writerow([None, None, None, cleaned_tweet])
        #print(cleaned_tweet)

