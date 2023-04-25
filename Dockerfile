FROM python:3.11

COPY ./src /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "-m", "http.server", "8080"]
