import sqlite3
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, "database.db")

# create the database
def create_database():

    # Connect to database
    connection = sqlite3.connect(DATABASE_PATH)
    # Create cursor
    cursor = connection.cursor()

    # Create table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ReviewHistory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        review TEXT,
        prediction TEXT,
        confidence REAL,
        sentiment TEXT,
        date TEXT
    )
    """)

    # Save changes
    connection.commit()
    # Close connection
    connection.close()

# save the data into the database
def save_prediction(review, prediction, confidence,sentiment, date):

    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO ReviewHistory
    (review, prediction, confidence,sentiment,date)
    VALUES (?, ?, ?, ?, ?)
    """, (review, prediction, confidence,sentiment,date))

    connection.commit()
    connection.close()

# get search and filter of review history 
def get_history_paginated(search="", filter_by="All", page=1, per_page=10):

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    conditions = []
    parameters = []

    # Search
    if search:
        conditions.append("review LIKE ?")
        parameters.append(f"%{search}%")

    # Filter
    if filter_by and filter_by != "All":
        conditions.append("prediction = ?")
        parameters.append(filter_by)

    # WHERE clause
    where_clause = ""

    if conditions:
        where_clause = "WHERE " + " AND ".join(conditions)

    # --------------------------------
    # TOTAL RECORDS
    # --------------------------------

    cursor.execute(
        f"""
        SELECT COUNT(*)
        FROM ReviewHistory
        {where_clause}
        """,
        parameters
    )

    total_records = cursor.fetchone()[0]

    # --------------------------------
    # PAGINATION
    # --------------------------------

    offset = (page - 1) * per_page

    cursor.execute(
        f"""
        SELECT *
        FROM ReviewHistory
        {where_clause}
        ORDER BY id DESC
        LIMIT ? OFFSET ?
        """,
        parameters + [per_page, offset]
    )

    reviews = cursor.fetchall()

    connection.close()

    # Calculate total pages
    total_pages = (total_records + per_page - 1) // per_page

    return reviews, total_pages


# dashboard data
def get_dashboard_data():

    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    # Total reviews
    cursor.execute("SELECT COUNT(*) FROM ReviewHistory")
    total = cursor.fetchone()[0]

    # Genuine reviews
    cursor.execute("""
        SELECT COUNT(*)
        FROM ReviewHistory
        WHERE prediction = '✅ Genuine Review'
    """)
    genuine = cursor.fetchone()[0]

    # Fake reviews
    cursor.execute("""
        SELECT COUNT(*)
        FROM ReviewHistory
        WHERE prediction = '❌ Fake Review'
    """)
    fake = cursor.fetchone()[0]

    # Positive Reviews
    cursor.execute("""
    SELECT COUNT(*)
    FROM ReviewHistory
    WHERE sentiment='😊 Positive'
    """)
    positive = cursor.fetchone()[0]

    # Neutral Reviews
    cursor.execute("""
    SELECT COUNT(*)
    FROM ReviewHistory
    WHERE sentiment='😐 Neutral'
    """)
    neutral = cursor.fetchone()[0]

    # Negative Reviews
    cursor.execute("""
    SELECT COUNT(*)
    FROM ReviewHistory
    WHERE sentiment='😞 Negative'
    """)
    negative = cursor.fetchone()[0]

    connection.close()

    return {
        "total": total,
        "genuine": genuine,
        "fake": fake,
        "positive": positive,
        "neutral": neutral,
        "negative": negative
    }


# images generate charts
def generate_charts():

    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute(
    "SELECT COUNT(*) FROM ReviewHistory WHERE prediction='❌ Fake Review'"
    )

    fake = cursor.fetchone()[0]

    cursor.execute(
    "SELECT COUNT(*) FROM ReviewHistory WHERE prediction='✅ Genuine Review'"
    )

    genuine = cursor.fetchone()[0]

    cursor.execute(
    "SELECT COUNT(*) FROM ReviewHistory WHERE sentiment='😊 Positive'"
    )
    positive = cursor.fetchone()[0]

    cursor.execute(
    "SELECT COUNT(*) FROM ReviewHistory WHERE sentiment='😐 Neutral'"
    )
    neutral = cursor.fetchone()[0]

    cursor.execute(
    "SELECT COUNT(*) FROM ReviewHistory WHERE sentiment='😞 Negative'"
    )
    negative = cursor.fetchone()[0]

    connection.close()

    os.makedirs("static/charts", exist_ok=True)

    # Pie Chart
    plt.figure(figsize=(5,5))

    plt.pie(
        [fake, genuine],
        labels=["Fake","Genuine"],
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Fake vs Genuine Reviews")

    plt.savefig("static/charts/pie_chart.png")
    plt.close()

    # Bar Chart
    plt.figure(figsize=(6,4))

    plt.bar(
        ["Fake","Genuine"],
        [fake, genuine]
    )

    plt.title("Review Count")
    plt.ylabel("Number of Reviews")

    plt.savefig("static/charts/bar_chart.png")
    plt.close()

    # Sentiment Pie Chart
    counts = [positive, neutral, negative]
    labels = ["Positive", "Neutral","Negative"]

    # Remove categories with zero reviews
    filtered_counts = []
    filtered_labels = []

    for count, label in zip(counts, labels):
        if count > 0:
            filtered_counts.append(count)
            filtered_labels.append(label)

    plt.figure(figsize=(6,6))

    plt.pie(
        filtered_counts,
        labels=filtered_labels,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.legend(filtered_labels, loc="best")

    plt.title("Review Sentiment Distribution")

    plt.savefig("static/charts/sentiment_chart.png")

    plt.close()

# Export data of database of excel and pdf
def get_all_history():

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id,review,
               prediction,
               confidence,
               sentiment,
               date
        FROM ReviewHistory
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    connection.close()

    return rows

# review_details
def get_review_by_id(review_id):

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM ReviewHistory
        WHERE id = ?
    """, (review_id,))

    review = cursor.fetchone()

    connection.close()

    return review


# confidence graph data
def get_confidence_data():

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, confidence, date
        FROM ReviewHistory
        ORDER BY id ASC
    """)

    rows = cursor.fetchall()
    connection.close()
    data = []

    for row in rows:
        data.append({
            "id": row["id"],
            "confidence": float(row["confidence"]),
            "date": row["date"]
        })
    return data

    
create_database()

print("Database Created Successfully")