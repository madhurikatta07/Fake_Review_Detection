# import re
# import string
# import nltk
# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer

# # Auto-download required NLTK resources
# def download_nltk_resources():
#     resources = ['stopwords', 'wordnet', 'omw-1.4', 'punkt']
#     for resource in resources:
#         try:
#             # Check if the resource is already available
#             if resource == 'punkt':
#                 nltk.data.find('tokenizers/punkt')
#             elif resource == 'stopwords':
#                 nltk.data.find('corpora/stopwords')
#             elif resource == 'wordnet':
#                 nltk.data.find('corpora/wordnet')
#             elif resource == 'omw-1.4':
#                 nltk.data.find('corpora/omw-1.4')
#         except LookupError:
#             try:
#                 nltk.download(resource, quiet=True)
#             except Exception as e:
#                 print(f"Warning: Failed to download NLTK resource '{resource}': {e}")

# # Try downloading resources on load
# download_nltk_resources()

# # Load stopwords and lemmatizer safely
# try:
#     STOPWORDS = set(stopwords.words('english'))
# except Exception:
#     try:
#         nltk.download('stopwords', quiet=True)
#         STOPWORDS = set(stopwords.words('english'))
#     except Exception:
#         STOPWORDS = set()

# try:
#     lemmatizer = WordNetLemmatizer()
# except Exception:
#     try:
#         nltk.download('wordnet', quiet=True)
#         lemmatizer = WordNetLemmatizer()
#     except Exception:
#         lemmatizer = None

# def clean_text(text):
#     """
#     Cleans, normalizes, and tokenizes raw review text.
#     - Removes HTML tags
#     - Removes URLs/emails
#     - Removes punctuation and numbers
#     - Lowers casing
#     - Removes stopwords
#     - Performs lemmatization
#     """
#     if not isinstance(text, str):
#         return ""
    
#     # 1. Lowercase
#     text = text.lower()
    
#     # 2. Remove HTML tags
#     text = re.sub(r'<[^>]+>', ' ', text)
    
#     # 3. Remove URLs
#     text = re.sub(r'https?://\S+|www\.\S+', ' ', text)
    
#     # 4. Remove emails
#     text = re.sub(r'\S+@\S+', ' ', text)
    
#     # 5. Remove punctuation, replacing with space to prevent words sticking together
#     translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
#     text = text.translate(translator)
    
#     # 6. Remove numbers
#     text = re.sub(r'\d+', ' ', text)
    
#     # 7. Tokenize, remove stopwords, and lemmatize
#     tokens = text.split()
#     cleaned_tokens = []
    
#     for word in tokens:
#         # Filter out short tokens and stopwords
#         if len(word) > 2 and word not in STOPWORDS:
#             if lemmatizer:
#                 try:
#                     word = lemmatizer.lemmatize(word)
#                 except Exception:
#                     pass
#             cleaned_tokens.append(word)
            
#     return " ".join(cleaned_tokens)




import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def clean_reviews(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r"http\S+|www\S+", "", text)   # Remove URLs
    text = re.sub(r"<.*?>", "", text)  # Remove HTML tags
    text = re.sub(r"[^a-zA-Z\s]", "", text)   # Remove punctuation and numbers
    words = word_tokenize(text)    # Tokenize
    # Remove stopwords and perform lemmatization
    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if word not in stop_words
    ]
    return " ".join(words)  # Join words back into a sentence
    