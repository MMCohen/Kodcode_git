import uvicorn
from fastapi import FastAPI
import reports

app = FastAPI()

@app.get("/stats/summary")
def get_summary():
  return reports.get_summary()


@app.get("/stats/units")
def count_by_unit():
    return reports.count_by_unit()


@app.get("/stats/understaffed")
def get_units_with_multiple_soldiers():
    return reports.get_units_with_multiple_soldiers()




if __name__ == "__main__":
    uvicorn.run(app)
