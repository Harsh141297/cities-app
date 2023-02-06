FROM python:3.9-slim-buster

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY cities-app.py .

CMD ["python", "cities-app.py"]
