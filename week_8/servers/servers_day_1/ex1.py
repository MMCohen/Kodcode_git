from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def get_ping():
    return {"status": "pong"}

@app.get("/greet/{user_name}")
def greet(user_name):
    return {"msg": f"hello, {user_name}!"}


