from fastapi import FastAPI
from models import BloodTestInput, DiagnosisOutput
from services.ai_model import predict

app = FastAPI(title="DiagnoAI Backend")

@app.post("/diagnosis", response_model=DiagnosisOutput)
def diagnose(data: BloodTestInput):
    result = predict(data)
    return result