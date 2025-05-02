from fastapi import FastAPI
from pydantic import BaseModel
from inference import predict

app = FastAPI()

class QARequest(BaseModel):
    question: str
    context: str

@app.post("/predict")
def get_prediction(request: QARequest):
    answer = predict(request.question, request.context)
    return {"answer": answer}