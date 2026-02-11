import streamlit as st
import pickle
import os
import sys

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
try:
    from src.preprocessing import clean_text
except ImportError:
    from preprocessing import clean_text

# Load Model
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../data/model.pkl')

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        return None
    with open(MODEL_PATH, 'rb') as f:
        return pickle.load(f)

model = load_model()

st.title("🎬 Movie Review Sentiment Analysis")
st.write("Enter a movie review below to classify it as **Positive** or **Negative**.")

# Input
user_input = st.text_area("Review Text:", height=150, placeholder="Example: This movie was fantastic! ...")

if st.button("Analyze Sentiment"):
    if not model:
        st.error("Model not found! Please run `src/model.py` to train the model first.")
    elif user_input:
        # Preprocess
        cleaned_text = clean_text(user_input)
        
        # Predict
        prediction = model.predict([cleaned_text])[0]
        probs = model.predict_proba([cleaned_text])[0]
        
        # Display
        if prediction == 'positive':
            st.success(f"### Sentiment: Positive 😊")
            st.write(f"Confidence: {probs[1]*100:.2f}%")
        else:
            st.error(f"### Sentiment: Negative 😠")
            st.write(f"Confidence: {probs[0]*100:.2f}%")
    else:
        st.warning("Please enter some text.")

# Footer / About
st.markdown("---")
st.caption("UAS Kecerdasan Buatan - Sentiment Analysis Project")
