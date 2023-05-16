import os
from fastapi import FastAPI

app = FastAPI()

def get_env_message():
    return os.environ.get("ENV_MESSAGE") or "Nothing to report"


def get_secret_message():
    return os.environ.get("SECRET_MESSAGE") or "Nothing lurking"


@app.get("/")
def home_view():
    return  {"hello": "world", "cron": "smooth-cronjob", "watchtower": "working", "env-message": get_env_message(), "secret-message": get_secret_message()}
