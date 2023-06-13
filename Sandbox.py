import nltk
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer


sid = SentimentIntensityAnalyzer()         


print(sid.polarity_scores("its good!"))
print(sid.polarity_scores("its good"))
