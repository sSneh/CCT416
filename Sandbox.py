import nltk
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sentence = 'whole thread glad didnt sign sag yet actor along writer need protected paid people going using ai actor image people going huge problem'


sid = SentimentIntensityAnalyzer()         


print(sid.polarity_scores("it should've been good"))
print(sid.polarity_scores("been good"))
