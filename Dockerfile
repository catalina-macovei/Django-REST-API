FROM python:3.12.2-slim-bullseye

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x django.sh

EXPOSE 8000

ENTRYPOINT ["/app/django.sh"]
