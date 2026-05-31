from fastapi import FastAPI

app = FastAPI()

@app.get("/calc/{a}/{op}/{b}")
def calculator(a, op, b):
    try:
        match op:
            case "add":
                calculated_value = f"{int(a) + int(b)}"
            case "sub":
                calculated_value = f"{int(a) - int(b)}"
            case "mul":
                calculated_value = f"{int(a) * int(b)}"
            case "div":
                calculated_value = f"{int(a) / int(b)}"
    except ValueError:
        raise
    return {f"operation": {op}, "result": {calculated_value}}