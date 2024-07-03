FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Copy the database initialization script and make it executable
COPY init_db.sh /app/init_db.sh
RUN chmod +x /app/init_db.sh

# Run the database initialization script
RUN /app/init_db.sh

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
