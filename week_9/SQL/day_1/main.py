import uvicorn
from fastapi import FastAPI
import db
import setup
app = FastAPI()


@app.post("/setup")
def status():
    setup.setup()
    return {"status": "ok"}


@app.get("/schema")
def schema():
    data = db.get_schema()
    return data


@app.get("/soldiers")
def get_all_soldiers():
    return {"soldiers": []}


@app.get("/health")
def get_health():
    return {"db": "connected", "table": "soldiers"}



if __name__ == "__main__":
    uvicorn.run(app)

