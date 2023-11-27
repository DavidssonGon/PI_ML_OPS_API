from fastapi import FastAPI
import uvicorn
from funciones.pi_functions import  PlayTimeGenre, UserForGenre, UsersRecommend, UsersWorstDeveloper, sentiment_analysis

app = FastAPI()

@app.get('/')
def hola():
    return {'API en proceso'}

@app.get('/PlayTimeGenre/genero/{genero}')
async def imput_genero(genero:str):
    resultado = PlayTimeGenre(genero)
    return resultado
