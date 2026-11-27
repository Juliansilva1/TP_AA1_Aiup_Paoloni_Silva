"""Predice si mañana llueve a partir de las mediciones del día.

Uso:
    python inferencia.py entrada.csv salida.csv

La entrada tiene las mediciones del día con las mismas columnas que el dataset
original (Date, Location, MinTemp, ...). La salida es el mismo CSV con dos
columnas nuevas: la probabilidad de lluvia y la predicción (Yes / No).
"""

import json
import sys
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from tensorflow import keras

CARPETA = Path(__file__).parent


def preparar_variables(datos):
    """Los mismos pasos de limpieza y del mes que se aplicaron en el notebook."""
    datos = datos.copy()
    datos['Cloud9am'] = datos['Cloud9am'].replace(9.0, np.nan)
    datos['Cloud3pm'] = datos['Cloud3pm'].replace(9.0, np.nan)
    mes = pd.to_datetime(datos['Date']).dt.month
    datos['Month_sin'] = np.sin(2 * np.pi * mes / 12)
    datos['Month_cos'] = np.cos(2 * np.pi * mes / 12)
    return datos


def main():
    if len(sys.argv) != 3:
        sys.exit('Uso: python inferencia.py entrada.csv salida.csv')
    entrada, salida = sys.argv[1], sys.argv[2]

    # Lo aprendido en el entrenamiento: preprocesamiento, red y umbral. Acá no se entrena nada
    preprocesamiento = joblib.load(CARPETA / 'preprocesamiento.joblib')
    red = keras.models.load_model(CARPETA / 'red_neuronal.keras')
    with open(CARPETA / 'umbral.json') as archivo:
        umbral = json.load(archivo)['umbral']

    datos = pd.read_csv(entrada)

    # Las columnas salen del pipeline guardado, no de una lista escrita a mano
    columnas = list(preprocesamiento.feature_names_in_)
    variables = preprocesamiento.transform(preparar_variables(datos)[columnas])

    probabilidad = red.predict(variables, verbose = 0).flatten()
    datos['probabilidad_lluvia'] = probabilidad.round(3)
    datos['llueve_manana'] = np.where(probabilidad >= umbral, 'Yes', 'No')

    datos.to_csv(salida, index = False)
    print(f"{len(datos)} predicciones guardadas en {salida} (umbral {umbral}).")


if __name__ == '__main__':
    main()
