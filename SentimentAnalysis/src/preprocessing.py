import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Download NLTK data (run once)
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

def clean_text(text):
    """
    Cleans text by:
    1. Removing HTML tags
    2. Removing non-letters
    3. Lowercasing
    4. Removing stopwords
    """
    # 1. Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    
    # 2. Remove non-letters and numbers (keep only alphabets)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # 3. Convert to lower case
    text = text.lower()
    
    # 4. Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = text.split()
    cleaned_words = [w for w in words if w not in stop_words]
    
    return " ".join(cleaned_words)
