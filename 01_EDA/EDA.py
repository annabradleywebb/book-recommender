from bs4 import BeautifulSoup
import nltk
import re
import string
from nltk.tokenize import word_tokenize

nltk.download('wordnet')
lemmatizer = nltk.stem.WordNetLemmatizer()

def clean_ratings_dist(df, ratings_column):
    clean = df[ratings_column].str.split("|", n=5, expand = True)
    df["5-star"] = clean[0]
    df["4-star"] = clean[1]
    df["3-star"] = clean[2]
    df["2-star"] = clean[3]
    df["1-star"] = clean[4]
    df["total"] = clean[5]
    return df

def clean_ratings_dist_2(df, ratings_column):
    df = df.drop([ratings_column], axis=1)
    df["5-star"] = df["5-star"].str[2::]
    df["4-star"] = df["4-star"].str[2::]
    df["3-star"] = df["3-star"].str[2::]
    df["2-star"] = df["2-star"].str[2::]
    df["1-star"] = df["1-star"].str[2::]
    df["total"] = df["total"].str[6::]
    return df


def clean_gr_description(df, description_column):
    for i in range(len(df)):
        try:
            soup = BeautifulSoup(df[description_column][i])
            df[description_column][i] = soup.get_text()
        except TypeError:
            pass
    return df

def lower_clean(text):
    clean_text = re.sub('[^a-zA-Z]', " ", text)
    clean_text = clean_text.lower()
    return clean_text

def clean_description(df, description_column):
    for i in range(len(df)):
        try:
            df[description_column][i] = lower_clean(df[description_column][i])
        except TypeError:
            pass
    return df

def word_tokenize_description(df, text):
    df['word_tokenized_description'] = 0
    for i in range(len(df)):
        try:
            df['word_tokenized_description'][i] = nltk.word_tokenize(df[text][i])
        except TypeError:
            pass
    return df

def lemmatize_nouns(text):
    lemmatized = [lemmatizer.lemmatize(word, pos="n") for word in text]
    return lemmatized

def lemmatize_verbs(text):
    lemmatized = [lemmatizer.lemmatize(word, pos="v") for word in text]
    return lemmatized

def lemmatized_column(df):
    df['lemmatized_description'] = 0
    for i in range(len(df)):
        try:
            df['lemmatized_description'][i] = lemmatize_nouns(df['word_tokenized_description'][i])
            df['lemmatized_description'][i] = lemmatize_verbs(df['lemmatized_description'][i])
            df['lemmatized_description'][i] = ' '.join(df['lemmatized_description'][i])
        except TypeError:
            pass
    return df