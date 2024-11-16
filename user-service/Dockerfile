FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_APP=app.py

ENV DATABASE_URL=postgresql://postgres:postgres@postgres-db:5432/mydb

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

