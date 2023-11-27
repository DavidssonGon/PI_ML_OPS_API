from fastapi import FastAPI
import uvicorn
from funciones.pi_functions import  PlayTimeGenre, UserForGenre, UsersRecommend, UsersWorstDeveloper, sentiment_analysis

app = FastAPI()

@app.get('/')
def hola():
    return {'API en proceso'}

@app.get('/PlayTimeGenre/genero/{genero}')
async def imput_genero_def1(genero:str):
    try:
        resultado_def1 = PlayTimeGenre(genero)
        return resultado_def1
    except Exception as e:
        return {'Error': str(e)}
    
    
@app.get('/UserForGenre/genero/{genero}')
async def imput_genero_def2(genero:str):
    try:
        resultado_def2 = UserForGenre(genero)
        return resultado_def2
    except Exception as e:
        return {'Error': str(e)}
    
    
@app.get('/UsersRecommend/anio/{anio}')
async def imput_anio_def3(anio:int):
    try:
        anio_int = int(anio)
    except ValueError:
        return {"detail": [{"type": "invalid_input", "msg": "El año debe ser un número entero"}]}
     
    resultado_def3 = UsersRecommend(anio_int)
    return resultado_def3
      
      
@app.get('/UsersWorstDeveloper/anio/{anio}')
async def imput_anio_def4(anio:int):
    try:
        anio_int = int(anio)
    except ValueError:
        return {"detail": [{"type": "invalid_input", "msg": "El año debe ser un número entero"}]}
     
    resultado_def4 = UsersWorstDeveloper(anio_int)
    return resultado_def4

@app.get('/sentiment_analysis/desarrolladora/{desarrolladora}')
async def imput_desarrolladora_def5(desarrolladora:str):
    try:
        resultado_def5 = sentiment_analysis(desarrolladora)
        return resultado_def5
    except Exception as e:
        return {'Error': str(e)}

    