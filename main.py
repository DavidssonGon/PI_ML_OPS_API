from fastapi import FastAPI
import uvicorn
import os
from funciones.pi_functions import  PlayTimeGenre, UserForGenre, UsersRecommend, UsersWorstDeveloper, sentiment_analysis, recomendacion_juego
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get('/', response_class=HTMLResponse)
def hola():
    html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>API DE CONSULTAS STEAM</title>
            <style>
                body {
                    font-family: 'Open Sans', sans-serif;
                    background-color: #121212; /* Fondo oscuro */
                    color:  #E2E2E2; /* Color de texto claro */
                    margin: 20px;
                    line-height: 1.6;
                }

                h1, h2 {
                    color: #3498db; /* Color de los encabezados */
                    text-shadow: 1px 1px 2px #111; /* Sombra para resaltar los encabezados */
                }

                 ul {
                    list-style: none; /* Quita los puntos de la lista */
                    padding: 0;
                }

                li {
                    margin-bottom: 15px;
                }

                a {
                    color: #2980b9; /* Color del enlace */
                    text-decoration: none;
                    font-weight: bold;
                }

                a:hover {
                    background-color: #154360; /* Cambia el color de fondo al pasar el ratón */
                    text-decoration: underline; /* Mantén el subrayado al pasar el ratón */
                }
            </style>
        </head>
        <body>

            <h1>API DE CONSULTAS STEAM </h1>

            <p>Me presento, soy Davidsson Gonzalez el creador detrás de esta vaina</p>
            <p>En esta API se ofrecen consultas específicas y muy curiosas sobre la plataforma de juegos STEAM, pero no solamente hay información sobre juegos también sobre usuarios, métricas, reseñas y recomendaciones. </p>

            <h2>Consultas Disponibles:</h2>

            <ul>
                <li><strong><a href="/PlayTimeGenre/genero/Action">/PlayTimeGenre/genero/{genero} </a></strong>: Devuelve el <strong>año</strong> con más horas jugadas para el género especificado.                             </li>
                <li><strong><a href="/UserForGenre/genero/Indie">/UserForGenre/genero/{genero} </a></strong>: Devuelve el <strong>usuario</strong> con más horas jugadas para el género especificado.</li>
                <li><strong><a href="/UsersRecommend/anio/2012">/UsersRecommend/anio/{anio} </a></strong>: Devuelve el top 3 de <strong>juegos</strong> MÁS recomendados por usuarios para el año especificado.</li>
                <li><strong><a href="/UsersWorstDeveloper/anio/2016">/UsersWorstDeveloper/anio/{anio} </a></strong>: Devuelve el top 3 de <strong>juegos</strong> MENOS recomendados por usuarios para el año especificado.</li>
                <li><strong><a href="/sentiment_analysis/desarrolladora/ubisoft">/sentiment_analysis/desarrolladora/{desarrolladora} </a></strong>: Devuelve una listalista con la cantidad total de registros de reseñas de usuarios para la <strong>desarrolladora</strong> especificada.</li>
                <li><strong><a href="/recomendacion_juego/id/70">/recomendacion_juego/id/{id_producto} </a></strong>: Devuelve una lista con 5 juegos <strong>recomendados</strong> en base al id del juego especificado.</li>
            </ul>

            <p>(Puedes hacer click sobre cualquier endpoint para probarlo)</p>

            <h2>Menú interactivo:</h2>
            <ul>
                <li><strong><a href="/docs">/docs </a></strong>: También puedes entrar a este link donde accederás a un menú interactivo con todas las consultas disponibles.                             </li>
            </ul>
            <p>Encontraras una interfaz gráfica donde encontraras todas las funciones, si despliegas sus menús podrás ingresar datos crackeando en el cuadro a la derecha que dice <strong>“Try it out”</strong> luego podrás ingresar datos en el cuadro ubicado justo debajo de donde dice <strong>“Description”</strong> recuerda ingresar el tipo de dato específico para cada consulta, espero que disfrutes de mi API. </p>


            <p>Si se presenta algún inconveniente con la API házmelo saber.</p>


        </body>
    </html>
"""
    return HTMLResponse(content=html_content)


@app.get('/PlayTimeGenre/genero/{genero}')
async def ingresa_un_genero_def1(genero:str):
    try:
        resultado_def1 = PlayTimeGenre(genero)
        return resultado_def1
    except Exception as e:
        return {'Error': str(e)}
    
    
@app.get('/UserForGenre/genero/{genero}')
async def ingresa_un_genero_def2(genero:str):
    try:
        resultado_def2 = UserForGenre(genero)
        return resultado_def2
    except Exception as e:
        return {'Error': str(e)}
    
    
@app.get('/UsersRecommend/anio/{anio}')
async def ingresa_un_año_def3(anio:int):
    try:
        anio_int = int(anio)
    except ValueError:
        return {"detail": [{"type": "invalid_input", "msg": "El año debe ser un número entero"}]}
     
    resultado_def3 = UsersRecommend(anio_int)
    return resultado_def3
      
      
@app.get('/UsersWorstDeveloper/anio/{anio}')
async def ingresa_un_año_def4(anio:int):
    try:
        anio_int = int(anio)
    except ValueError:
        return {"detail": [{"type": "invalid_input", "msg": "El año debe ser un número entero"}]}
     
    resultado_def4 = UsersWorstDeveloper(anio_int)
    return resultado_def4

@app.get('/sentiment_analysis/desarrolladora/{desarrolladora}')
async def ingresa_una_desarrolladora_def5(desarrolladora:str):
    try:
        resultado_def5 = sentiment_analysis(desarrolladora)
        return resultado_def5
    except Exception as e:
        return {'Error': str(e)}
    

@app.get('/recomendacion_juego/id/{id_producto}')
async def ingresa_un_id_def6(id_producto:int):
    try:
        id_int = int(id_producto)
    except ValueError:
        return {"detail": [{"type": "invalid_input", "msg": "El id de producto debe ser un número entero (744570)"}]}
    
    resultado_def6 = recomendacion_juego(id_int)
    return resultado_def6   


@app.post('/recomendacion_juego')
async def ingresa_un_id(id_producto: int):
    try:
        id_int = int(id_producto)
    except ValueError:
        return {"detail": [{"type": "invalid_input", "msg": "El id de producto debe ser un número entero (744570)"}]}
    
    resultado_def6 = recomendacion_juego(id_int)
    return resultado_def6