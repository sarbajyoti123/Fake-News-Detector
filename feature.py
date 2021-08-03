import numpy as np # linear algebra
import pandas as pd #data processing

import os
import re
import nltk

import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
from nltk.stem import WordNetLemmatizer
import re

def get_all_query(title):
    total= title
    total = [total]
    return total

def remove_punctuation_stopwords_lemma(sentence):
    filter_sentence = ''
    lemmatizer=WordNetLemmatizer()
    sentence = re.sub(r'[^\w\s]','',s)
    words = nltk.word_tokenize(sentence) #tokenization
    words = [w for w in words if not w in stop_words]
    for word in words:
        filter_sentence = filter_sentence + ' ' + str(lemmatizer.lemmatize(word)).lower()
    return filter_sentence
