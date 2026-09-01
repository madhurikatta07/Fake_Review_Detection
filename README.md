# 🤖 AI Fake Review Detection

An AI-powered web application that analyzes online product reviews and predicts whether a review is **Genuine** or **Fake** using Machine Learning.

The application also performs **sentiment analysis**, stores prediction history in a SQLite database, provides a dashboard with analytical charts, supports search and filtering, and allows users to export prediction history as CSV and PDF files.

---

## 1. 📌 Project Title

**AI Fake Review Detection**

---

## 2. 📝 Project Description

Online reviews play an important role in influencing customer purchasing decisions. However, fake and deceptive reviews can mislead customers and negatively affect businesses.

The **AI Fake Review Detection** system uses Natural Language Processing (NLP) and Machine Learning to analyze the textual content of a review and classify it as either:

* ✅ **Genuine Review**
* ❌ **Fake Review**

The application provides a simple web interface where users can enter a review and receive a prediction along with its confidence score.

In addition, the system provides:

* Review sentiment analysis
* Prediction history
* Search and filtering
* Review details
* Dashboard analytics
* Fake/Genuine review statistics
* CSV export
* PDF export

---

## 3. ✨ Features

### 🔍 Fake Review Prediction

Users can enter a product or service review and the system predicts whether it is:

* **Genuine**
* **Fake**

### 📊 Confidence Score

The application displays the confidence associated with the prediction.

Example:

```text
Prediction: Genuine Review
Confidence: 74.08%
```

### 😊 Sentiment Analysis

The system analyzes the sentiment expressed in the review.

Possible sentiment categories include:

* Positive
* Negative
* Neutral

### 📜 Prediction History

Every prediction can be stored in the SQLite database.

The history page displays information such as:

* Review
* Prediction
* Confidence
* Date

### 🔎 Search and Filtering

Users can search prediction history and filter reviews based on their classification.

For example:

```text
All
Genuine
Fake
```

### 📈 Dashboard

The dashboard provides an overview of prediction activity using:

* Total reviews
* Genuine reviews
* Fake reviews
* Pie chart
* Bar chart
* Sentiment chart

### 📄 Review Details

Users can view detailed information about an individual prediction.

### 📥 Export Reports

Prediction history can be exported as:

* CSV
* PDF

### 🔐 Login

The application includes a login interface for controlled access to application functionality.

### 📱 Responsive Interface

The application is designed to work across different screen sizes using HTML and CSS.

---

## 4. 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### Machine Learning

* Scikit-learn
* TF-IDF Vectorization
* Machine Learning classification model

### Natural Language Processing

* NLTK
* Text preprocessing
* Stopword removal
* Lemmatization

### Database

* SQLite

### Data Processing

* Pandas
* NumPy

### Visualization

* Matplotlib

### Development Tools

* Jupyter Notebook
* Git
* GitHub
* VS Code

---

## 5. 📁 Project Structure

```text
FakeReviewDetection/
│
├── .env
├── .gitignore
├── Procfile
├── README.md
├── app.py
├── database.py
├── database.db
├── requirements.txt
│
├── dataset/
│   ├── README.md
│   ├── clean_reviews.csv
│   ├── fake reviews dataset.csv
│   └── preprocessed_reviews.csv
│
├── exports/
│   ├── .gitkeep
│   ├── history.pdf
│   └── prediction_history.csv
│
├── models/
│   ├── model.pkl
│   └── tfidf.pkl
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Preprocessing.ipynb
│   └── 03_Model_Comparison.ipynb
│
├── screenshots/
│   ├── home.png
│   ├── result.png
│   ├── history.png
│   ├── dashboard.png
│   └── login.png
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── main.js
│   │
│   └── charts/
│       ├── bar_chart.png
│       ├── pie_chart.png
│       └── sentiment_chart.png
│
├── templates/
│   ├── dashboard.html
│   ├── history.html
│   ├── index.html
│   ├── login.html
│   ├── navbar.html
│   ├── result.html
│   └── review_details.html
│
└── utils/
    ├──__init__.py
    ├── preprocess.py
    └── sentiment.py
```

### Important Directories

**`dataset/`**
Contains the original, cleaned, and preprocessed review datasets.

**`models/`**
Contains the trained Machine Learning model and TF-IDF vectorizer.

**`notebooks/`**
Contains notebooks used for exploratory data analysis, preprocessing, and model comparison.

**`templates/`**
Contains Flask HTML templates.

**`static/`**
Contains CSS, JavaScript, and generated charts.

**`utils/`**
Contains reusable preprocessing and sentiment-analysis functions.

**`exports/`**
Stores generated CSV and PDF prediction-history files.

---

## 6. 🤖 ML Model

The project uses **Natural Language Processing and Machine Learning** for fake review classification.

### Text Preprocessing

Before prediction, the review is cleaned using NLP techniques such as:

1. Convert text to lowercase
2. Remove URLs
3. Remove HTML tags
4. Remove punctuation
5. Remove numbers
6. Remove unnecessary whitespace
7. Remove stopwords
8. Perform lemmatization

Example:

```text
Original:
"This product is AMAZING!!! Visit https://example.com"

Processed:
"product amazing"
```

### TF-IDF Vectorization

The cleaned review is converted into numerical features using:

**TF-IDF — Term Frequency-Inverse Document Frequency**

The trained vectorizer is stored in:

```text
models/tfidf.pkl
```

### Classification Model

The trained classification model is stored in:

```text
models/model.pkl
```

The application loads the trained model and TF-IDF vectorizer when making predictions.

### Model Evaluation

The model is evaluated using common classification metrics:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

Previously evaluated model results achieved approximately:

```text
Accuracy  : 87.07%
Precision : 86.60%
Recall    : 87.61%
F1-Score  : 87.11%
```

> These values depend on the dataset split and trained model version.

---

## 7. 📊 Dataset

The project uses a **deceptive/fake review dataset** for training and evaluating the Machine Learning model.

The dataset files are maintained inside:

```text
dataset/
```

### Dataset Files

```text
dataset/
├── README.md
├── clean_reviews.csv
├── fake reviews dataset.csv
└── preprocessed_reviews.csv
```

The dataset contains review text along with classification information used to train the fake-review detection model.

### Dataset Processing Pipeline

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Text Preprocessing
     ↓
TF-IDF Vectorization
     ↓
Train/Test Split
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Saved Model
```

The processed data is stored in:

```text
clean_reviews.csv
preprocessed_reviews.csv
```

---

## 8. ⚙️ Installation

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
```

Move into the project directory:

```bash
cd FakeReviewDetection
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 3: Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Download NLTK Resources

If required, download the NLTK resources used by the preprocessing system:

```python
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
```

---

## 9. ▶️ How to Run

After installing the dependencies, start the Flask application:

```bash
python app.py
```

The application will normally be available at:

```text
http://127.0.0.1:5000
```

Open the address in your browser.

### Basic Workflow

```text
Open Application
       ↓
Enter Review
       ↓
Submit Review
       ↓
Text Preprocessing
       ↓
TF-IDF Transformation
       ↓
ML Prediction
       ↓
Sentiment Analysis
       ↓
Display Result
       ↓
Save Prediction
       ↓
View History / Dashboard
```

---

## 10. 🔮 How Prediction Works

The prediction process consists of several stages.

### Step 1: User Input

The user enters a review through the web interface.

Example:

```text
"The product quality is excellent and I am very happy with my purchase."
```

### Step 2: Text Preprocessing

The review is passed to the preprocessing module:

```text
utils/preprocess.py
```

The text is cleaned and normalized.

### Step 3: TF-IDF Transformation

The processed review is converted into numerical features using the saved TF-IDF vectorizer:

```text
models/tfidf.pkl
```

### Step 4: ML Prediction

The transformed text is passed to the trained Machine Learning model:

```text
models/model.pkl
```

### Step 5: Classification

The model produces a classification result:

```text
Fake
```

or

```text
Genuine
```

### Step 6: Confidence

The application calculates/displays the prediction confidence when supported by the trained model.

Example:

```text
Prediction: Genuine Review
Confidence: 74.08%
```

### Step 7: Sentiment Analysis

The review is also analyzed to determine its sentiment.

```text
Sentiment: Positive
```

### Step 8: Database Storage

The prediction details are stored in the SQLite database.

---

## 11. 🗄️ Database

The project uses **SQLite** for storing prediction history.

The database file is:

```text
database.db
```

Database-related operations are handled through:

```text
database.py
```

### Prediction History

The database stores information such as:

| Field      | Description                  |
| ---------- | ---------------------------- |
| ID         | Unique prediction identifier |
| Review     | User-submitted review        |
| Prediction | Fake or Genuine              |
| Confidence | Prediction confidence        |
| Sentiment  | Prediction sentiment         |
| Date       | Prediction date/time         |

### Database Workflow

```text
User submits review
        ↓
Prediction generated
        ↓
Prediction saved
        ↓
SQLite database
        ↓
History page
        ↓
Dashboard / Reports
```

The stored data is also used for generating statistics and exports.

---

## 12. 📸 Screenshots

Screenshots of the application can be added here to demonstrate the major pages.

### 🏠 Home / Prediction Page

Add screenshot:

```text
screenshots/home.png
```

The home page allows users to enter a review and submit it for analysis.

### 🎯 Prediction Result

Add screenshot:

```text
screenshots/result.png
```

Displays:

* Fake/Genuine prediction
* Confidence score
* Sentiment

### 📜 Prediction History

Add screenshot:

```text
screenshots/history.png
```

Displays previously analyzed reviews.

### 📊 Dashboard

Add screenshot:

```text
screenshots/dashboard.png
```

Displays:

* Total reviews
* Genuine reviews
* Fake reviews
* Prediction charts
* Sentiment statistics

### 🔎 Review Details

Add screenshot:

```text
screenshots/review-details.png
```

Displays detailed information about an individual prediction.

> **Note:** Create a `screenshots/` folder and add your actual project screenshots before publishing the final README.

---

## 13. 🚀 Future Enhancements

The project can be improved further with the following features:

* 🔥 Deep Learning models such as LSTM/BERT
* 🤖 Transformer-based fake review detection
* 🌐 Multilingual review detection
* 📱 Mobile application
* ☁️ Cloud deployment
* 🔐 Improved authentication and authorization
* 📊 Real-time analytics
* 🔗 Product-review URL analysis
* 🛒 Integration with e-commerce platforms
* 🧠 Explainable AI for prediction reasoning
* 📈 Advanced model comparison
* 🗂️ Larger and more diverse datasets
* ⚡ Real-time review monitoring
* 🛡️ Detection of coordinated review campaigns

---

## 14. 👩‍💻 Author

**Madhuri Katta**

B.Tech — Computer Science & Engineering (Artificial Intelligence)

Passionate about Artificial Intelligence, Machine Learning, Python, and Web Application Development.

This project demonstrates the practical experience in:

* Machine Learning
* Natural Language Processing
* Python and Flask
* SQLite Database Management
* Data Analysis and Visualization
* Full-Stack Web Application Development

🔗 Connect With Me
GitHub: https://github.com/madhurikatta07
LinkedIn: https://www.linkedin.com/in/madhurikatta07
Email: [madhukatta0731@gmail.com]
---

## ⭐ Project Highlights

```text
🤖 AI-based Fake Review Detection
📝 NLP-based Text Processing
🔍 Fake vs Genuine Review Classification
😊 Sentiment Analysis
📊 Interactive Dashboard & Analytics
🗄️ SQLite Prediction History
📜 Search & Filter Prediction History
📥 CSV & PDF Report Export
🌐 Flask Web Application
📈 Machine Learning Model Evaluation
