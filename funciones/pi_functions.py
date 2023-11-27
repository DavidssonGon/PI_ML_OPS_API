import numpy as np
import pandas as pd

consulta1 = 'E:\\AAADATOS\Henry\\AA_Data_Science\\MATERIAL_PI\\PI_ML_OPS_API\\DataSet\\PlayTimeGenre.gzip'
consulta2 = 'E:\\AAADATOS\Henry\\AA_Data_Science\\MATERIAL_PI\\PI_ML_OPS_API\\DataSet\\UserForGenre.gzip'
consulta3 = 'E:\\AAADATOS\Henry\\AA_Data_Science\\MATERIAL_PI\\PI_ML_OPS_API\\DataSet\\UsersRecommend.gzip'
consulta4 = 'E:\\AAADATOS\Henry\\AA_Data_Science\\MATERIAL_PI\\PI_ML_OPS_API\\DataSet\\UsersWorstDeveloper.gzip'
consulta5 = 'E:\\AAADATOS\Henry\\AA_Data_Science\\MATERIAL_PI\\PI_ML_OPS_API\\DataSet\\sentiment_analysis.gzip'

# Función N°1
def PlayTimeGenre(genero):

    if not isinstance(genero, str):
        return {'Error': 'El género debe ser una cadena (string)'}
    
    df_def1 = pd.read_csv(consulta1, compression='gzip')

    df_genero = df_def1[df_def1['Genres'].str.contains(genero, case=False, na=False)]

    df_agrupado = df_genero.groupby('Year_Launch')['Playtime_Forever_Hours'].sum().reset_index()

    if df_agrupado.empty:
        return {'Error': f'No hay datos para el género "{genero}" después de filtrar por año'}

    anio_mas_jugado = df_agrupado.loc[df_agrupado['Playtime_Forever_Hours'].idxmax()]['Year_Launch']

    resultado = {'Año de lanzamiento con más horas jugadas para Género {}'.format(genero): int(anio_mas_jugado)}
    
    return resultado


# Función N°2
def UserForGenre(genero):
    
    if not isinstance(genero, str):
        return {'Error': 'El género debe ser una cadena (string)'}

    df_def2 = pd.read_csv(consulta2, compression='gzip')

    df_genero = df_def2[df_def2['Genres'].str.contains(genero, case=False, na=False)]

    if df_genero.empty:
        return {'Error': f'No hay datos para el género "{genero}"'}

    df_agrupado_usuario = df_genero.groupby('User_Id')['Playtime_Forever_Hours'].sum().reset_index()

    if df_agrupado_usuario.empty:
        return {'Error': f'No hay datos para el género "{genero}" después de filtrar por usuario'}

    usuario_mas_horas = df_agrupado_usuario.loc[df_agrupado_usuario['Playtime_Forever_Hours'].idxmax()]['User_Id']

    df_agrupado_anio = df_genero.groupby('Year_Launch')['Playtime_Forever_Hours'].sum().reset_index()

    lista_acumulacion_horas = [{'Año': int(anio), 'Horas': int(horas)} for anio, horas in zip(df_agrupado_anio['Year_Launch'],
                                                                                              df_agrupado_anio['Playtime_Forever_Hours'])]
    
    resultado = {
        'Usuario con más horas jugadas para Género {}'.format(genero): usuario_mas_horas,
        'Horas jugadas': lista_acumulacion_horas
    }

    return resultado


# Función N°3
def UsersRecommend(anio):

    if not isinstance(anio, int):
        return {'Error': 'El año debe ser un entero'}

    df_def3 = pd.read_csv(consulta3, compression='gzip')

    df_anio = df_def3[df_def3['Year'] == anio]

    if df_anio.empty:
        return [{'Error': f'No hay datos para el año {anio}'}]

    df_agrupado_juegos = df_anio.groupby('Title')['Conteo'].sum().reset_index()

    df_agrupado_juegos = df_agrupado_juegos.sort_values(by='Conteo', ascending=False)

    top_3_juegos = df_agrupado_juegos.head(3)

    resultado = [
        {'Puesto 1': top_3_juegos.iloc[0]['Title']},
        {'Puesto 2': top_3_juegos.iloc[1]['Title']},
        {'Puesto 3': top_3_juegos.iloc[2]['Title']}
    ]

    return resultado


# Función N°4
def UsersWorstDeveloper(anio):

    if not isinstance(anio, int):
        return {'Error': 'El año debe ser un entero'}

    df_def4 = pd.read_csv(consulta4, compression='gzip')

    df_anio = df_def4[df_def4['Year'] == anio]

    if df_anio.empty:
        return [{'Error': f'No hay datos para el año {anio}'}]

    df_agrupado_desarrolladoras = df_anio.groupby('Developer')['Conteo'].sum().reset_index()

    df_agrupado_desarrolladoras = df_agrupado_desarrolladoras.sort_values(by='Conteo', ascending=False)

    top_3_desarrolladoras = df_agrupado_desarrolladoras.head(3)

    resultado = [
        {"Puesto 1": top_3_desarrolladoras.iloc[0]['Developer']},
        {"Puesto 2": top_3_desarrolladoras.iloc[1]['Developer']},
        {"Puesto 3": top_3_desarrolladoras.iloc[2]['Developer']}
    ]
    
    return resultado


# Función N°5

def sentiment_analysis(desarrolladora):
    
    # Se verifica que la desarrolladora sea una cadena (string)
    if not isinstance(desarrolladora, str):
        return {'Error': 'La Desarrolladora debe ser una cadena (string)'}
    
    # Se inicializa el Data Frame al que se le hara la consulta
    df_def5 = pd.read_csv(consulta5, compression='gzip')
    
    # Se filtra el DataFrame para incluir solo las filas correspondientes a la desarrolladora dada
    df_desarrolladora = df_def5[df_def5['Developer'] == desarrolladora]
    
    # Se verifica si el DataFrame resultante está vacío
    if df_desarrolladora.empty:
        return {'Error': f'No hay datos para la desarrolladora {desarrolladora}'}
    
    # Se realiza un mapeo de valores originales a equivalentes deseados
    mapeo_sentimientos = {0: "Negative", 1: "Neutral", 2: "Positive"}
    
    # Se reemplaza los valores originales por los equivalentes deseados
    df_desarrolladora['Sentiment_Analysis'] = df_desarrolladora['Sentiment_Analysis'].map(mapeo_sentimientos)
    
    # Se define la lista ordenada de sentimientos
    sentimientos_ordenados = ["Negative", "Neutral", "Positive"]
    
    # Se agrupa por "Sentiment_Analysis" y cuenta la frecuencia de cada valor
    conteo_sentimientos = df_desarrolladora['Sentiment_Analysis'].value_counts().reindex(sentimientos_ordenados, fill_value=0).to_dict()
    
    # Se construye el diccionario de resultado con etiquetas
    resultado = {desarrolladora: {f"{sentimiento} =": conteo_sentimientos[sentimiento] for sentimiento in sentimientos_ordenados}}
    
    return resultado
