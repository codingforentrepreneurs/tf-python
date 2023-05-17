FROM python:3.11

COPY ./src /app
WORKDIR /app

RUN pip install -r requirements.txt

# CMD ["python", "-m", "http.server", "8080"]

CMD ["gunicorn", "main:app", "--workers", "1", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8080"]