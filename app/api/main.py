from fastapi import FastAPI
from mangum import Mangum
app = FastAPI()

@app.get("/")
async def root():
    return{"message":"Hola el moreno"}

handler = Mangum(app=app)