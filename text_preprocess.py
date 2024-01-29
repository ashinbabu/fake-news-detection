# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer
# import string



# # Download NLTK resources
# nltk.download('stopwords')

# # Function to preprocess a text string
# def preprocess_text(input_text):
#     # Lowercasing
#     text = input_text.lower()

#     # Removing punctuation
#     text = ''.join([char for char in text if char not in string.punctuation])

#     # Removing stop words
#     stop_words = set(stopwords.words('english'))
#     text = ' '.join([word for word in text.split() if word.lower() not in stop_words])

#     # Stemming
#     stemmer = PorterStemmer()
#     text = ' '.join([stemmer.stem(word) for word in text.split()])

#     return text


import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
import langid  # Import langid library

# Download NLTK resources
nltk.download('stopwords')

# Function to preprocess a text string and remove non-English words
def preprocess_text(input_text):
    # Lowercasing
    text = input_text.lower()

    # Removing punctuation
    text = ''.join([char for char in text if char not in string.punctuation])

    # Removing stop words
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word.lower() not in stop_words])

    # Detect language for each word and keep only English words
    words = text.split()
    english_words = [word for word in words if langid.classify(word)[0] == 'en']

    # Stemming
    stemmer = PorterStemmer()
    english_words_stemmed = [stemmer.stem(word) for word in english_words]

    return ' '.join(english_words_stemmed)
