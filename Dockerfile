FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY etlpytthon.py .
COPY Hate_Crimes_2017-2025.csv .

CMD ["python", "etlpytthon.py"]
