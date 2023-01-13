import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer
nltk.download('punkt')
Stemmer = PorterStemmer()

def tokenize(comando):
    return nltk.word_tokenize(comando)
def stem(word):
    return Stemmer.stem(word.lower())

def bag_of_words(tokenized_comando,words):
    comando_word = [stem(word) for word in tokenized_comando]
    bag = np.zeros(len(words),dtype=np.float32)

    for idx , w in enumerate(words):
        if w in comando_word:
            bag[idx] = 1

        
    return bag

