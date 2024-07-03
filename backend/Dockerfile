FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Ensure the database initialization script is executable
RUN chmod +x init_db.sh

# Run the database initialization script
RUN ./init_db.sh

CMD ["python", "app.py"]
