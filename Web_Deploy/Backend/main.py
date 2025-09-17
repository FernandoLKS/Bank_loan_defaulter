from fastapi import FastAPI
from routers import predict  
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Propensão à Oferta")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"msg": "API funcionando!"}

app.include_router(predict.router)