import string
import unicodedata
from joblib import load
import pandas as pd
import os
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def tokenize(data: pd.DataFrame):
    data['Words'] = data['Review'].apply(word_tokenize)
    return data


class TextProcessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('spanish'))
        self.lemmatizer = WordNetLemmatizer()
        self.stemmer = SnowballStemmer('spanish')
        self.punctuation = string.punctuation

    def to_lowercase(self, texto):
        return [word.lower() for word in texto]

    def remove_punctuation(self, texto):
        return [word for word in texto if word not in self.punctuation]

    def remove_triple_punctuation(self, texto):
        return [word for word in texto if word != '...']

    def remove_stopwords(self, texto):
        return [word for word in texto if word not in self.stop_words]

    def lemmatize(self, texto):
        return [self.lemmatizer.lemmatize(word) for word in texto]

    def stem(self, texto):
        return [self.stemmer.stem(word) for word in texto]

    def remove_non_ascii(self, texto):
        return [unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore') for word in texto]

    def preprocess(self, texto):
        texto = self.to_lowercase(texto)
        texto = self.remove_punctuation(texto)
        texto = self.remove_triple_punctuation(texto)
        texto = self.remove_stopwords(texto)
        texto = self.lemmatize(texto)
        texto = self.stem(texto)
        texto = self.remove_non_ascii(texto)
        return texto


def clean_process(data: pd.DataFrame):
    processor = TextProcessor()
    data['Stemmed words'] = [processor.preprocess(
        text) for text in data['Words']]
    return data


def clean_vectorize(data: pd.DataFrame, vectorizer):
    data['Text'] = [' '.join(text) for text in data['Stemmed words']]
    x_etiquetado = vectorizer.transform(data['Text'])
    data.drop(['Text', 'Words', 'Stemmed words'], axis=1, inplace=True)
    return x_etiquetado


def predict(review):
    location = os.path.dirname(os.path.abspath(__file__))
    fullpath = os.path.join(location, 'model.joblib')
    pipeline = load(fullpath)

    new_data = pd.DataFrame({'Review': [review]})

    return pipeline.predict(new_data)[0]
