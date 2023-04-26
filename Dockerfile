FROM python:3.10.10

COPY ./src /app

WORKDIR /app

RUN pip install pip --upgrade
RUN pip install -r requirements.txt

CMD ["python", "-m", "http.server", "8080"]
