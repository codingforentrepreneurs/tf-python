import os
import subprocess
import time

import requests

def test_gunicorn_start():
    gunicorn_process = subprocess.Popen(
        ["gunicorn", "-w", "1", "-k", "uvicorn.workers.UvicornWorker", "main:app", "-b", "127.0.0.1:8000"]
    )
    time.sleep(2)  # Give Gunicorn some time to start

    try:
        response = requests.get("http://127.0.0.1:8000")
        assert response.status_code == 200
        assert response.json() == {
            "hello": "world",
            "cron": "smooth-cronjob",
            "watchtower": "working",
            "env-message": os.environ.get("ENV_MESSAGE") or "Nothing to report",
        }
    finally:
        gunicorn_process.terminate()
        gunicorn_process.wait()
