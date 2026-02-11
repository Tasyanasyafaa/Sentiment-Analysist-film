import pandas as pd
import numpy as np
import pickle
import os
import requests
import sys

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Ensure src module can be imported if needed, but we run this as script
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
try:
    from src.preprocessing import clean_text
except ImportError:
    # If running from same dir
    from preprocessing import clean_text

DATA_URL = "https://raw.githubusercontent.com/Ankit152/IMDB-sentiment-analysis/master/IMDB-Dataset.csv"
DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/IMDB-Dataset.csv')
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../data/model.pkl')

def download_data():
    if os.path.exists(DATA_PATH):
        print("Dataset already exists.")
        return pd.read_csv(DATA_PATH)
    
    print(f"Downloading dataset from {DATA_URL}...")
    try:
        response = requests.get(DATA_URL)
        response.raise_for_status()
        
        # Ensure data directory exists
        os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
        
        with open(DATA_PATH, 'wb') as f:
            f.write(response.content)
        print("Download complete.")
        return pd.read_csv(DATA_PATH)
    except Exception as e:
        print(f"Failed to download dataset: {e}")
        print("Falling back to NLTK movie_reviews (small dataset)...")
        import nltk
        try:
            nltk.data.find('corpora/movie_reviews')
        except LookupError:
            nltk.download('movie_reviews')
        from nltk.corpus import movie_reviews
        
        documents = [(list(movie_reviews.words(fileid)), category)
                     for category in movie_reviews.categories()
                     for fileid in movie_reviews.fileids(category)]
        
        # Convert to DataFrame format
        df = pd.DataFrame(documents, columns=['text_list', 'sentiment'])
        df['review'] = df['text_list'].apply(lambda x: " ".join(x))
        df = df[['review', 'sentiment']]
        return df

def train_and_save_model():
    df = download_data()
    
    # Take a sample if dataset is too huge for quick local training (e.g. 10k)
    # df = df.sample(10000, random_state=42) 
    
    print("Preprocessing data (this may take a while)...")
    # Apply cleaning
    df['clean_review'] = df['review'].apply(clean_text)
    
    X = df['clean_review']
    y = df['sentiment']
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Pipeline
    pipeline = Pipeline([
        ('vect', CountVectorizer()),
        ('tfidf', TfidfTransformer()),
        ('clf', MultinomialNB()),
    ])
    
    print("Training model...")
    pipeline.fit(X_train, y_train)
    
    print("Evaluating model...")
    y_pred = pipeline.predict(X_test)
    
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    
    # Save model
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(pipeline, f)
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    train_and_save_model()
