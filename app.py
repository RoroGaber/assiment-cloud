import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
nltk.download('stopwords')
# Get the English stop words list from NLTK
stop_words = set(stopwords.words('english'))

def remove_stop_words(text):
    # Tokenize the text into words
    words = word_tokenize(text)
    # Remove stop words from the text
    non_stop_words = [word for word in words if word.lower() not in stop_words]
    return non_stop_words

def count_word_occurrences(words):
    # Count the occurrences of each word in the list
    word_counts = Counter(words)
    return word_counts
with open("random_paragraphs.txt", "r") as file:
    text = file.read()

non_stop_words = remove_stop_words(text)
word_counts = count_word_occurrences(non_stop_words)

# Display the remaining words and their counts side by side
for word, count in word_counts.items():
    print(f"{word}: {count}")
