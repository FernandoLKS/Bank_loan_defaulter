from fastapi import APIRouter
from schemas.client import ClientData
from services.prediction_service import predict_client

router = APIRouter()

@router.post("/predict")
def predict(data: ClientData):
    resultado = predict_client(data, threshold=0.68)
    return {"Propício a aceitar a oferta?": bool(resultado)}