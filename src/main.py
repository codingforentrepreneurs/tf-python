import os
from fastapi import FastAPI

app = FastAPI()

ENV_MESSAGE = os.environ.get("ENV_MESSAGE") or "Nothing to report"

@app.get("/")
def home_view():
    return  {"hello": "world", "cron": "smooth-cronjob", "watchtower": "working", "env-message": ENV_MESSAGE}
