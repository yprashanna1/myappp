import json
import re
from transformers import pipeline
import spacy
import nltk

# Download necessary NLTK data
nltk.download('punkt')

# Load the SpaCy model
nlp = spacy.load('en_core_web_sm')

# Load the pre-trained DistilGPT-2 model for text generation
model_name = "distilgpt2"
generator = pipeline("text-generation", model=model_name, tokenizer=model_name)

def load_rules(file_path='rules.json'):
    """
    Load ethical rules from a JSON file.
    """
    with open(file_path, 'r') as file:
        rules_data = json.load(file)
    return rules_data

def save_rules(rules_data, file_path='rules.json'):
    """
    Save ethical rules to a JSON file.
    """
    with open(file_path, 'w') as file:
        json.dump(rules_data, file, indent=4)

def get_ai_response(prompt):
    """
    Generate AI response using the pre-trained model.
    """
    response = generator(prompt, max_length=150, num_return_sequences=1, truncation=True)[0]['generated_text']
    return response

