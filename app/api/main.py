from fastapi import FastAPI
from mangum import Mangum


app = FastAPI()

@app.get("/")
async def root():
    return{"message":"Hola el mo"}

@app.get("/docs")
def read_docs():
    return {"docs": "Este es el punto de documentación de FastAPI."}

handler = Mangum(app=app)