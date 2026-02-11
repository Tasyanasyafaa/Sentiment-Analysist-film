import pandas as pd
import pickle
import os
import sys
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
try:
    from src.preprocessing import clean_text
except ImportError:
    from preprocessing import clean_text

DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/IMDB-Dataset.csv')
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../data/model.pkl')

def evaluate():
    if not os.path.exists(MODEL_PATH):
        print("Model not found.")
        return

    print("Loading data...")
    # Load a smaller sample for quick evaluation if needed, or full
    try:
        df = pd.read_csv(DATA_PATH)
        # We need to replicate the split to get the test set
        # Note: This is imperfect if random_state wasn't fixed in model.py, 
        # but model.py used random_state=42.
        
        df['clean_review'] = df['review'].apply(clean_text)
        X = df['clean_review']
        y = df['sentiment']
        
        _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        print("Loading model...")
        with open(MODEL_PATH, 'rb') as f:
            pipeline = pickle.load(f)
            
        print("Predicting...")
        y_pred = pipeline.predict(X_test)
        
        acc = accuracy_score(y_test, y_pred)
        print(f"Accuracy: {acc:.4f}")
        print("Report:\n", classification_report(y_test, y_pred))
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    evaluate()
