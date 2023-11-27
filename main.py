from fastapi import FastAPI
import uvicorn
from funciones.pi_functions import  PlayTimeGenre, UserForGenre, UsersRecommend, UsersWorstDeveloper, sentiment_analysis

app = FastAPI()

@app.get('/')
def hola():
    return {'Bienvenidos a mi api'}

@app.get('/PlayTimeGenre/{genero}')
async def imput_genero(genero:str):
    resultado = PlayTimeGenre(genero)
    return resultado
