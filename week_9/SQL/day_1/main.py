import uvicorn
from fastapi import FastAPI
from db import get_schema
app = FastAPI()


@app.post("/setup")
def status():
    return {"status": "ok"}


@app.get("/schema")
def schema():
    data = get_schema()
    return data


@app.get("/soldiers")
def get_all_soldiers():
    return {"soldiers": []}


@app.get("/health")
def get_health():
    return {"db": "connected", "table": "soldiers"}



if __name__ == "__main__":
    uvicorn.run(app)

