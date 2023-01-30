import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.preprocessing import LabelEncoder

# natural language toolkit 
import nltk
import gensim

# regular expression
import re
import string

#preprocessing tools
from nltk.stem import WordNetLemmatizer
from gensim.parsing.preprocessing import remove_stopwords
from gensim.utils import tokenize

nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

def clean(text):
    text = text.lower() # нижний регистр
    text = re.sub(r'http\S+', " ", text) # удаляем ссылки
    text = re.sub(r'@\w+',' ',text) # удаляем упоминания пользователей
    text = re.sub(r'#\w+', ' ', text) # удаляем хэштеги
    text = re.sub(r'\d+', ' ', text) # удаляем числа
    text = re.sub(r' <br /><br />', ' ', text)
    #['' for i in text if i in string.punctuation]
    text = text.translate(str.maketrans('', '', string.punctuation))
    # text = re.sub(r'<.*?>',' ', text) # 
    return text

def tokenize_text(text):
    tokenize_text = list(tokenize(text))
    return tokenize_text

wn_lemmatizer = WordNetLemmatizer()

# nltk.download('wordnet')

from nltk.corpus import wordnet

def nltk_tag_to_wordnet_tag(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

def lemmatize_sentence(sentence):
    #tokenize the sentence and find the POS tag for each token
    nltk_tagged = nltk.pos_tag(sentence)
    #tuple of (token, wordnet_tag)
    wordnet_tagged = map(lambda x: (x[0], nltk_tag_to_wordnet_tag(x[1])), nltk_tagged)
    lemmatized_sentence = []
    for word, tag in wordnet_tagged:
        if tag is None:
            #if there is no available tag, append the token as is
            lemmatized_sentence.append(word)
        else:
            #else use the tag to lemmatize the token
            lemmatized_sentence.append(wn_lemmatizer.lemmatize(word, tag))
    return " ".join(lemmatized_sentence)