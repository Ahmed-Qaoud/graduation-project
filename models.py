from pydantic import BaseModel

class BloodTestInput(BaseModel):
    hemoglobin: float
    wbc: float
    platelets: float

class DiagnosisOutput(BaseModel):
    prediction: str
    confidence: float
