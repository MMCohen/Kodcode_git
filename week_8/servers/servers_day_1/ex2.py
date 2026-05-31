from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def version():
    return {"service": "my-api", "version": "1.0"}


@app.get("/users/admin")
def admin():
    return {"role": "admin", "access": "full"}


@app.get("/users/{user_id}")
def user_info(user_id):
    return {"user_id": user_id,
            "name": "John",
            "email": f"John_{user_id}@gmail.com"}
