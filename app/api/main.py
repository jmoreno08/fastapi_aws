from fastapi import FastAPI
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

# Configurar CORS
origins = [
    "http://localhost:5173",
    "https://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*", "access-control-allow-methods", "access-control-allow-origin", "authorization", "content-type"],
)

@app.get("/")
async def root():
    return{"message":"Hola el mo"}


handler = Mangum(app=app)