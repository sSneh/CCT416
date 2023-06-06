import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer

#https://towardsdatascience.com/tf-idf-for-document-ranking-from-scratch-in-python-on-real-world-dataset-796d339a4089

# Load the cleaned  dataset
johntory_df = pd.read_csv('inputs/Cleaned_Step2.csv')

# Replace missing values with empty strings
johntory_df['cleaned_tweet'] = johntory_df['cleaned_tweet'].fillna('')

# Extract the text
docs = johntory_df['cleaned_tweet'].tolist()

# Create a TfidfVectorizer object with custom settings
tfidf = TfidfVectorizer(
    max_features=1000, # Only consider the top 1000 most important words
    stop_words='english' # Remove common English stop words
)

# Fit the TfidfVectorizer object to the data
tfidf.fit(docs)

# Get the TF-IDF scores for each word in the vocabulary
tfidf_scores = tfidf.idf_

# Get the feature names (i.e., the words in the vocabulary)
feature_names = tfidf.get_feature_names_out()

# Get the top 10 words by TF-IDF score
top_indices = tfidf_scores.argsort()[-10:][::-1]
top_words = [feature_names[i] for i in top_indices]
top_scores = [tfidf_scores[i] for i in top_indices]

# Normalize the scores to be between 0 and 1
max_score = max(top_scores)
top_scores = [score / max_score for score in top_scores]

# Create a bar chart of the top 10 words by TF-IDF score
fig, ax = plt.subplots(figsize=(5, 3))
ax.bar(top_words, top_scores)
ax.set_title('Top 10 Words by TF-IDF Score')
ax.set_xlabel('Words')
ax.set_ylabel('TF-IDF Score')
plt.xticks(rotation=45)
plt.show()

print(top_words)
print(top_indices)
print(top_scores)


# Transform the list of documents into a sparse matrix of TF-IDF values
tfidf_matrix = tfidf.transform(docs)

# Loop over the top words and find the indices of the documents that contain each word
for word in top_words:
    # Get the index of the word in the feature names array
    word_index = np.where(feature_names == word)[0][0]

    # Find the indices of the documents that contain the word
    doc_indices = tfidf_matrix[:, word_index].nonzero()[0]

    # Print the tweets that contain the word and their normalized TF-IDF scores
    for doc_index in doc_indices:
        tfidf_score = tfidf_matrix[doc_index, word_index]
        max_value = max(tfidf_matrix[doc_index,:]).toarray()[0]
        if max(max_value) != 0:  # <-- fix here
            normalized_tfidf_score = tfidf_score / max(max_value)
        else:
            normalized_tfidf_score = 0
        print(docs[doc_index])
        print(f"TF-IDF score: {normalized_tfidf_score}")
        print('---')
