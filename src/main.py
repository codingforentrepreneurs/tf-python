import os
from fastapi import FastAPI

app = FastAPI()

def get_env_message():
    return os.environ.get("ENV_MESSAGE") or "Nothing to report"


@app.get("/")
def home_view():
    return  {"hello": "world", "cron": "smooth-cronjob", "watchtower": "working", "env-message": get_env_message()}
