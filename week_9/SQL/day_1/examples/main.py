import uvicorn
from fastapi import FastAPI
import db

app = FastAPI()


@app.post("/setup")
def run_setup():
    # In real code this would call setup logic
    # For now just confirm
    return {"status": "setup triggered"}


@app.get("/schema")
def get_schema():
    columns = db.get_schema()
    print(columns)
    return {"columns": columns}


@app.get("/soldiers")
def get_all_soldiers():
    return {"soldiers": []}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)