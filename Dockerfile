FROM python:3.11

COPY requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# WORKDIR /app

COPY app.py .
COPY svc_classifier.pkl .

ENV MODE=dev

EXPOSE 5000

# ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "churn_predict:app"]
CMD ["python", "./app.py"]