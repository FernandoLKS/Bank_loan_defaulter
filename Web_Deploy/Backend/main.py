from fastapi import FastAPI
from routers import predict  

app = FastAPI(title="Propensão à Oferta")

@app.get("/")
def root():
    return {"msg": "API funcionando!"}

app.include_router(predict.router)