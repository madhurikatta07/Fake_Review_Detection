
# 🤖 AI Fake Review Detection

An AI/ML-powered web application that detects whether a product review is **Fake or Genuine** using Natural Language Processing (NLP) and Machine Learning.

The application analyzes review text, predicts its authenticity, provides a confidence score, performs sentiment analysis, stores prediction history, and presents analytical insights through a dashboard.

## 🌐 Live Demo

**Live Application:**
https://fake-review-detection-9i3d.onrender.com

**GitHub Repository:**
https://github.com/madhurikatta07/Fake_Review_Detection

---

## ✨ Features

* 🤖 Fake/Genuine review prediction
* 📊 Prediction confidence score
* 😊 Sentiment analysis
* 💾 Prediction history using SQLite
* 🔎 Search and filter prediction history
* 📈 Dashboard with prediction statistics and charts
* 📄 CSV and PDF report export
* 🔍 Individual review details
* 🔐 Login functionality
* 📱 Responsive web interface
* 🐳 Dockerized application
* ☁️ Render deployment

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap

### Backend

* Python
* Flask
* Gunicorn

### Machine Learning

* Scikit-learn
* TF-IDF Vectorization
* Machine Learning Classification
* NLTK
* Natural Language Processing

### Database

* SQLite
* SQLAlchemy

### Data Processing & Visualization

* Pandas
* NumPy
* Matplotlib

### Development & Deployment

* Jupyter Notebook
* Git
* GitHub
* Docker
* Render

---

## 🧠 Machine Learning

The application uses Natural Language Processing and Machine Learning to classify reviews.

### Text Preprocessing

The review text is processed using:

1. Lowercasing
2. URL removal
3. HTML tag removal
4. Punctuation removal
5. Number removal
6. Whitespace normalization
7. Stopword removal
8. Lemmatization

### TF-IDF Vectorization

After preprocessing, the review is converted into numerical features using **TF-IDF (Term Frequency-Inverse Document Frequency)**.

The trained vectorizer is stored in:

```text
models/tfidf.pkl
```

### Classification

The trained Machine Learning model is stored in:

```text
models/model.pkl
```

The model classifies a review as:

* ✅ **Genuine Review**
* ❌ **Fake Review**

---

## 📊 Model Performance

The evaluated model achieved approximately:

| Metric    |      Score |
| --------- | ---------: |
| Accuracy  | **87.07%** |
| Precision | **86.60%** |
| Recall    | **87.61%** |
| F1-Score  | **87.11%** |

The model was evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

> Performance values may vary depending on the dataset split and trained model version.

---

## 📊 Sentiment Analysis

In addition to fake-review classification, the application analyzes the sentiment expressed in the review.

Possible sentiment results include:

* 😊 Positive
* 😐 Neutral
* 😞 Negative

This provides additional insight into the review beyond its authenticity prediction.

---

## 🔄 Application Workflow

```text
User enters review
        ↓
Text preprocessing
        ↓
TF-IDF vectorization
        ↓
Machine Learning model
        ↓
Fake / Genuine prediction
        ↓
Confidence score
        ↓
Sentiment analysis
        ↓
Save prediction to SQLite
        ↓
Display result
        ↓
History / Dashboard / Reports
```

---

## 📈 Dashboard

The dashboard provides analytical insights into previously analyzed reviews.

It can display:

* Total reviews
* Genuine reviews
* Fake reviews
* Prediction distribution
* Sentiment statistics
* Charts and visualizations

This helps understand the overall prediction activity of the application.

---

## 📜 Prediction History

The application stores analyzed reviews in a SQLite database.

Stored information includes:

| Field      | Description           |
| ---------- | --------------------- |
| ID         | Unique prediction ID  |
| Review     | Submitted review      |
| Prediction | Fake or Genuine       |
| Confidence | Prediction confidence |
| Sentiment  | Review sentiment      |
| Date       | Prediction date/time  |

Users can search and filter the prediction history based on classification.

---

## 📥 Report Export

Prediction history can be exported for further analysis or reporting.

Supported formats:

* 📄 CSV
* 📑 PDF

---

## 📂 Project Structure

```text
## 5. 📁 Project Structure

```text
FakeReviewDetection/
│
├── .env
├── .gitignore
├── Procfile
├── Dockerfile
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

---

## 💻 Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/madhurikatta07/Fake_Review_Detection.git
```

### 2. Navigate to the Project

```bash
cd Fake_Review_Detection
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Download NLTK Resources

If they are not already available locally:

```python
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
```

### 7. Run the Application

```bash
python app.py
```

Open the application at:

```text
http://127.0.0.1:5000
```

---

## 🐳 Run with Docker

The project includes a Dockerfile for containerized deployment.

### Build the Docker Image

```bash
docker build -t fake-review-app .
```

### Run the Container

```bash
docker run -p 10000:10000 fake-review-app
```

Open:

```text
http://localhost:10000
```

### Docker Configuration

The application uses:

* **Python 3.12**
* NLTK resources installed during image build
* Gunicorn production server
* Dynamic `$PORT` support

The container starts the application using:

```text
gunicorn --bind 0.0.0.0:${PORT:-10000} --timeout 120 app:app
```

---

## ☁️ Deployment

The application is deployed using **Docker on Render**.

### Deployment Configuration

| Configuration     | Value                         |
| ----------------- | ----------------------------- |
| Platform          | Render                        |
| Deployment Method | Docker                        |
| Python            | 3.12                          |
| Web Server        | Gunicorn                      |
| Port              | Dynamic `$PORT`               |
| NLP Resources     | Installed during Docker build |

### Deployment Process

```text
GitHub Repository
       ↓
Dockerfile
       ↓
Render
       ↓
Docker Image Build
       ↓
Gunicorn
       ↓
Flask Application
       ↓
Live Web Application
```

### 🚀 Live Application

https://fake-review-detection-9i3d.onrender.com

---

## 📸 Screenshots

Add screenshots of the main application pages to a `screenshots/` directory.

Recommended screenshots:

```text
screenshots/
├── home.png
├── result.png
├── history.png
├── dashboard.png
└── login.png
```

Suggested README sections:

### 🏠 Home Page

Shows the interface where users enter a review for analysis.

### 🎯 Prediction Result

Shows:

* Fake/Genuine prediction
* Confidence score
* Sentiment

### 📜 Prediction History

Shows previously analyzed reviews and their prediction information.

### 📊 Dashboard

Shows prediction statistics and analytical charts.

### 🔎 Review Details

Shows detailed information about an individual prediction.

---

## 🗄️ Database

The application uses **SQLite** to store prediction history.

Database:

```text
database.db
```

Database operations are handled through:

```text
database.py
```

The stored prediction data is used by:

* Prediction History
* Dashboard
* Search and Filtering
* CSV Export
* PDF Export

> For production-scale deployment, a managed database such as PostgreSQL can be considered because SQLite is file-based.

---

## 🚀 Future Enhancements

* 🤖 Transformer-based fake-review detection
* 🧠 BERT-based NLP models
* 🌐 Multilingual review detection
* 📱 Mobile application
* 🗄️ PostgreSQL production database
* 📊 Advanced analytics
* 🔐 Improved authentication and authorization
* 🔗 Product-review URL analysis
* 🧠 Explainable AI
* 📈 Advanced model comparison
* 🗂️ Larger and more diverse datasets
* ⚡ Real-time review monitoring

---

## 👩‍💻 Author

### Madhuri Katta

**B.Tech — Computer Science & Engineering (Artificial Intelligence)**

Interested in:

* Artificial Intelligence
* Machine Learning
* Python Development
* Natural Language Processing
* Web Application Development

### Connect With Me

**GitHub:**
https://github.com/madhurikatta07

**LinkedIn:**
https://www.linkedin.com/in/madhurikatta07

**Email:**
[madhukatta0731@gmail.com](mailto:madhukatta0731@gmail.com)

---

## ⭐ Project Highlights

```text
🤖 AI/ML-based Fake Review Detection
📝 NLP Text Preprocessing
🔍 Fake vs Genuine Classification
📊 Confidence Score
😊 Sentiment Analysis
📈 Dashboard Analytics
💾 SQLite Prediction History
🔎 Search & Filtering
📥 CSV & PDF Export
🌐 Flask Web Application
🐳 Dockerized Deployment
☁️ Render Deployment
📊 87.07% Model Accuracy
```
