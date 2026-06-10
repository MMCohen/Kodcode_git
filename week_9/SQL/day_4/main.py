import uvicorn
from fastapi import FastAPI
import reports

app = FastAPI()

@app.get("/stats/summary")
def get_summary():
  return reports.get_summary()



if __name__ == "__main__":
    uvicorn.run(app)
