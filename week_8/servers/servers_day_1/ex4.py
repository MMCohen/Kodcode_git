from datetime import datetime

from fastapi import FastAPI

app = FastAPI()

@app.get("/status")
def status():
    return {"time": f"{datetime.now()}", "server": "fastAPI"}
