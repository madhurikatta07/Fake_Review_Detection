FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader -d /usr/local/share/nltk_data stopwords punkt wordnet omw-1.4

COPY . .

ENV NLTK_DATA=/usr/local/share/nltk_data

EXPOSE 10000

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT:-10000} --timeout 120 app:app"]