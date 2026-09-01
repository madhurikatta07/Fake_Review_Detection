
# Create the Flask Application
# from flask import Flask, render_template,request
from flask import Flask,request, render_template, flash, redirect, url_for, jsonify,session
import joblib
from datetime import datetime
# Import the Preprocessing Function
from utils.preprocess import clean_reviews
# import the database Function
from database import save_prediction, get_dashboard_data,generate_charts,get_all_history,get_review_by_id,get_history_paginated,get_confidence_data
# Import the sentiment Function
from utils.sentiment import analyze_sentiment
# export data to pdf and CSV
import csv
import os
from flask import send_file
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape

# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)

app = Flask(__name__)

load_dotenv()

app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key")

ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/tfidf.pkl")

@app.route("/")
def home():
    return render_template("index.html")

# PREDICT ROUTE
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get review from form
        review = request.form.get("review", "").strip()

        # Check empty review
        if not review:
            flash("Please enter a review.", "error")
            return redirect(url_for("home"))

        # Check minimum length
        if len(review) < 10:
            flash("Please enter at least 10 characters.","error")
            return redirect(url_for("home"))
        
        # TEXT PREPROCESSING
        cleaned_review = clean_reviews(review)
        # TF-IDF
        review_vector = vectorizer.transform([cleaned_review])
        # ML PREDICTION
        prediction = model.predict(review_vector)[0]
        # CONFIDENCE
        probabilities = model.predict_proba(review_vector)[0]
        confidence = round(float(probabilities[prediction]) * 100,2)
        # print("Prediction:", prediction)
        # print("Probabilities:", probabilities)
        # print("Confidence:", confidence)
        # CONVERT PREDICTION
        if prediction == 1:
            result = "✅ Genuine Review"
        else:
            result = "❌ Fake Review"
        # SENTIMENT ANALYSIS
        sentiment = analyze_sentiment(review)
        # print("Sentiment:", sentiment)
        # DATE
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # SAVE TO DATABASE
        save_prediction(
            review,
            result,
            confidence,
            sentiment,
            current_date
        )
        # RESULT PAGE
        return render_template(
            "result.html",
            prediction=result,
            confidence=confidence,
            sentiment=sentiment,
            review=review
        )

    except Exception as e:

        print("=" * 50)
        print("PREDICTION ERROR:")
        print(e)
        print("=" * 50)
        # print("Prediction Error:", e)
        flash(
            "Something went wrong. Please try again.",
            "error"
        )
        return redirect(url_for("home"))


 # history route
@app.route("/history")
def history():

    # Current page
    page = request.args.get("page", 1, type=int)
    # Reviews per page
    per_page = 25
    # Search value
    search = request.args.get("search", "").strip()
    # Filter value
    filter_by = request.args.get("filter", "All").strip()

    # Prevent invalid page numbers
    if page < 1:
        page = 1

    # Get paginated history
    reviews, total_pages = get_history_paginated(
        search=search,
        filter_by=filter_by,
        page=page,
        per_page=per_page
    )

    return render_template(
        "history.html",
        history=reviews,
        page=page,
        total_pages=total_pages,
        search=search,
        filter=filter_by
    )

# dashboard route
@app.route("/dashboard")
def dashboard():

    if not session.get("admin_logged_in"):
        flash("Please login to access the dashboard.", "warning")
        return redirect(url_for("login"))

    generate_charts()
    data = get_dashboard_data()

    return render_template(
        "dashboard.html",
        data=data
    )

# Export Route to csv
@app.route("/export")
def export_csv():

    """Exports prediction history to a CSV file and returns it for download"""

    rows = get_all_history()
    
    os.makedirs("exports", exist_ok=True)

    file_path = os.path.join("exports", "prediction_history.csv")

    with open(file_path, "w", newline="", encoding="utf-8") as csv_file:

        writer = csv.writer(csv_file)

        writer.writerow([
            "Review",
            "Prediction",
            "Confidence",
            "Sentiment",
            "Date"
        ])

        writer.writerows(rows)

    return send_file(
        file_path,
        as_attachment=True
    )

# Export data into pdf
@app.route("/export/pdf")
def export_pdf():

    rows = get_all_history()

    os.makedirs("exports", exist_ok=True)

    pdf_path = os.path.join(
        "exports",
        "history.pdf"
    )

    # Landscape A4 gives more horizontal space
    document = SimpleDocTemplate(
        pdf_path,
        pagesize=landscape(A4),
        rightMargin=20,
        leftMargin=20,
        topMargin=20,
        bottomMargin=20
    )

    styles = getSampleStyleSheet()

    title = Paragraph(
        "AI Fake Review Detection Report",
        styles["Title"]
    )

    elements = []

    elements.append(title)
    elements.append(Spacer(1, 15))

    # Style for table text
    table_style = ParagraphStyle(
        "TableText",
        parent=styles["Normal"],
        fontSize=8,
        leading=10
    )

    header_style = ParagraphStyle(
        "HeaderText",
        parent=styles["Normal"],
        fontSize=9,
        leading=11,
        textColor=colors.white,
        alignment=1
    )

    # Table Header
    table_data = [[
        Paragraph("Review", header_style),
        Paragraph("Prediction", header_style),
        Paragraph("Confidence", header_style),
        Paragraph("Sentiment", header_style),
        Paragraph("Date", header_style)
    ]]

    # Add database rows
    for row in rows:

        table_data.append([

            Paragraph(
                str(row[0]),
                table_style
            ),

            Paragraph(
                str(row[1]),
                table_style
            ),

            Paragraph(
                f"{row[2]}%",
                table_style
            ),

            Paragraph(
                str(row[4]),
                table_style
            ),

            Paragraph(
                str(row[3]),
                table_style
            )

        ])

    # Column widths
    table = Table(
        table_data,
        colWidths=[
            280,   # Review
            100,   # Prediction
            70,    # Confidence
            80,    # Sentiment
            100    # Date
        ],
        repeatRows=1
    )

    table.setStyle(TableStyle([
        # Header
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2563eb")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        # Alignment
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        # Grid
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        # Padding
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        # Body background
        ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),

    ]))

    elements.append(table)

    document.build(elements)

    return send_file(
        pdf_path,
        as_attachment=True
    )

# /review/<id> route for individual review details
@app.route("/review/<int:review_id>")
def review_details(review_id):

    review = get_review_by_id(review_id)

    if review is None:
        return "Review not found", 404

    return render_template(
        "review_details.html",
        review=review
    )

# confidence data 
@app.route("/confidence-data")
def confidence_data():

    data = get_confidence_data()
    return jsonify(data)

# login route
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:

            session["admin_logged_in"] = True

            flash("Login successful!", "success")

            return redirect(url_for("dashboard"))

        else:

            flash("Invalid username or password.", "danger")

    return render_template("login.html")


# Logout route
@app.route("/logout")
def logout():

    session.pop("admin_logged_in", None)

    flash("You have been logged out.", "success")

    return redirect(url_for("login"))


if __name__ == '__main__':
    
    # app.run(host='0.0.0.0', port=5000, debug=True)
    # app.run(debug=True)
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )

