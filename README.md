
# 🤖 AI Fake Review Detection

An AI-powered web application that analyzes online reviews and predicts whether a review is **Genuine** or **Fake** using Machine Learning.

The system also performs **Sentiment Analysis**, stores prediction history, provides search and filtering, generates reports, and displays analytical information through a dashboard.

---

## 📌 Problem Statement

Fake reviews can negatively affect customers and businesses by providing misleading information about products and services.

The purpose of this project is to develop a web-based system that uses Machine Learning and Natural Language Processing to analyze review text and identify whether the review is likely to be genuine or fake.

The application also provides sentiment analysis to determine whether the review is Positive, Negative, or Neutral.

---

# ✨ Features

### 🏠 Home Page

- Enter a product or service review
- Detect review authenticity
- Loading spinner while prediction is running
- Input validation
- Error and success notifications

### 🤖 Fake Review Detection

- Machine Learning based prediction
- Genuine Review classification
- Fake Review classification
- Prediction confidence score

### 😊 Sentiment Analysis

- Positive sentiment
- Negative sentiment
- Neutral sentiment

### 📊 Prediction Result

Displays:

- Prediction result
- Confidence percentage
- Sentiment
- Original review

### 📜 Prediction History

- Store previous predictions
- Search reviews
- Filter Genuine/Fake reviews
- View individual review details
- Scrollable history table

### 📥 Export

- Export prediction history to CSV
- Export prediction history to PDF

### 📈 Dashboard

Displays:

- Total reviews
- Genuine reviews
- Fake reviews
- Positive reviews
- Negative reviews
- Neutral reviews
- Fake vs Genuine chart
- Sentiment distribution chart

### 🎨 User Interface

- Responsive design
- Mobile-friendly layout
- Modern cards
- Rounded corners
- Hover effects
- Loading animations
- Font Awesome icons
- Consistent navigation
- Footer

---

# 🏗️ Architecture

```text
                User
                  │
                  ▼
             Home Page
                  │
                  ▼
            Enter Review
                  │
                  ▼
          Flask Web Application
                  │
                  ▼
          Text Preprocessing
                  │
                  ▼
              TF-IDF
                  │
                  ▼
        Machine Learning Model
                  │
                  ▼
       Fake / Genuine Prediction
                  │
          ┌───────┴────────┐
          ▼                ▼
     Confidence       Sentiment
          │                │
          └───────┬────────┘
                  ▼
           SQLite Database
                  │
          ┌───────┼────────┐
          ▼       ▼        ▼
       History Dashboard Export



#🛠️ Tech Stack

# Frontend

HTML5
CSS3
JavaScript
Google Fonts
Font Awesome

#Backend

Python
Flask

# Machine Learning

Scikit-learn
TF-IDF Vectorization
Machine Learning Classification Model

NLP

Text preprocessing
NLTK
TextBlob
Sentiment Analysis

# Database

SQLite

# Data Visualization

Matplotlib

# Report Generation

ReportLab

# 📊 Dataset

The project uses a fake review dataset for training the Machine Learning model.

The dataset contains review text along with labels indicating whether the review is genuine or fake.

Before training, the review text is processed using Natural Language Processing techniques.

# Preprocessing includes:

Converting text to lowercase
Removing unnecessary characters
Removing URLs
Removing HTML tags
Removing punctuation
Removing stopwords
Lemmatization

# 🧠 Machine Learning Model

The project uses TF-IDF (Term Frequency-Inverse Document Frequency) to convert review text into numerical features.


Review
   ↓
Text Cleaning
   ↓
TF-IDF Vectorization
   ↓
Machine Learning Model
   ↓
Fake / Genuine

The trained model and TF-IDF vectorizer are saved inside the models directory.

Example:

models/
├── model.pkl
└── tfidf.pkl


# 📁 Folder Structure

FakeReviewDetection/
│
├── app.py
├── database.py
├── train_model.py
├── requirements.txt
├── README.md
├── database.db
│
├── dataset/
│   └── clean_reviews.csv
│
├── models/
│   ├── model.pkl
│   └── tfidf.pkl
│
├── templates/
│   ├── home.html
│   ├── result.html
│   ├── history.html
│   ├── dashboard.html
│   ├── review_details.html
│   └── navbar.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── main.js
│   │
│   └── charts/
│       ├── pie_chart.png
│       ├── bar_chart.png
│       └── sentiment_chart.png
│
└── exports/
    ├── history.csv
    └── history.pdf

The exact files may vary depending on the final version of the project.

# ⚙️ Installation

1. Clone the repository

git clone <YOUR-GITHUB-REPOSITORY-URL>

2. Open the project

cd FakeReviewDetection

3. Create a virtual environment

Windows: python -m venv venv

4. Activate the virtual environment

venv\Scripts\activate

5. Install dependencies

pip install -r requirements.txt

▶️ How to Run

Activate the virtual environment:venv\Scripts\activate

Run the Flask application: python app.py

The application will run at: http://127.0.0.1:5000

Open the URL in your browser.

🧪 Example
Input

This product is absolutely amazing and I really loved it.

Output

Prediction: Fake / Genuine
Confidence: XX%
Sentiment: Positive

The result depends on the trained Machine Learning model.

# 📜 Prediction History

Every successful prediction can be stored in the SQLite database.

The History page provides:

Search
   +
Filter
   ↓
Matching Reviews

Users can filter by:

All Reviews
Genuine Reviews
Fake Reviews

# 📥 Export Reports

Prediction history can be exported as:

CSV
/export
PDF
/export/pdf

The PDF report contains prediction information such as:

Review
Prediction
Confidence
Sentiment
Date

# 📈 Dashboard

The dashboard provides a visual overview of the stored predictions.

Review Statistics
Total Reviews
Genuine Reviews
Fake Reviews
Sentiment Statistics
Positive Reviews
Negative Reviews
Neutral Reviews
Charts
Fake vs Genuine Reviews
Review Distribution
Sentiment Distribution

# 🔐 Error Handling

The application handles common invalid inputs such as:

Empty review
Very short review
Invalid prediction requests
Unexpected prediction errors

Users receive friendly error messages instead of technical error pages.

# 📱 Responsive Design

The application is designed to work on:

Desktop
Laptop
Tablet
Mobile

The navigation, cards, buttons, forms, charts, and history table adapt to smaller screen sizes.

# 🚀 Future Enhancements

Possible future improvements include:

Deep Learning based fake review detection
Transformer models such as BERT
User authentication
Admin login
Product-wise review analysis
Review spam detection
Advanced analytics
Real-time review monitoring
Cloud deployment
REST API
Multi-language review detection
Improved model accuracy


# 🎯 Project Workflow

User
 ↓
Enter Review
 ↓
Text Preprocessing
 ↓
TF-IDF
 ↓
ML Prediction
 ↓
Fake / Genuine
 ↓
Confidence Score
 ↓
Sentiment Analysis
 ↓
Save to Database
 ↓
History
 ↓
Dashboard / Export


# 👩‍💻 Author

Madhuri Katta

B.Tech Computer Science & Engineering (Artificial Intelligence)




1. Project Title
2. Project Description
3. Features
4. Technologies Used
5. Project Structure
6. ML Model
7. Dataset
8. Installation
9. How to Run
10. How Prediction Works
11. Database
12. Screenshots
13. Future Enhancements
14. Author