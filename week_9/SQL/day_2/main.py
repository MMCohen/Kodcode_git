import db
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/soldiers")
def get_all_soldiers():
    db.get_all()
    pass

@app.get("/soldiers/{soldier_id}")
def get_by_id(soldier_id: int):
    db.get_by_id(soldier_id)
    pass

@app.put("/soldiers/{soldier_id}")
def update(soldier_id: int, data:dict):
    db.edit(soldier_id, data)
    pass

@app.delete("/soldiers/{soldier_id}")
def delete_soldier(soldier_id: int):
    db.delete(soldier_id)
    pass

@app.post("/soldiers")
def add_soldier(data: dict):
    db.create()

if __name__ == "__main__":
    uvicorn.run(app)
