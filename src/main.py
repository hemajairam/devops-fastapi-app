from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/predict")
def predict():
    return {"result": "DevOps success!"}
