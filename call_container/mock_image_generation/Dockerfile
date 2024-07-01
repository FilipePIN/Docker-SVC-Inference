FROM python:3.11

COPY requirements.txt .

RUN pip install -r requirements.txt
# RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# WORKDIR /app

COPY image_generation.py .

ENV MODE=dev

EXPOSE 6000

CMD ["python", "./image_generation.py"]