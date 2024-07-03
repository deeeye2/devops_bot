FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x init_db.sh
RUN ./init_db.sh

CMD ["python", "app.py"]
