# Predicción de lluvia en Australia · Docker

Imagen de Docker que predice, a partir de las mediciones de un día, si al día siguiente va a llover en cada ciudad. Usa la red neuronal elegida en el ítem 8 del notebook `TP_2/TP-clasificacion-AA1.ipynb`.

## Contenido de la carpeta

| Archivo | Qué es |
|---|---|
| `Dockerfile` | La receta para armar la imagen. |
| `requirements.txt` | Las librerías que necesita la inferencia, con su versión. |
| `inferencia.py` | Carga los archivos del modelo y predice. No entrena. |
| `preprocesamiento.joblib` | Imputación, codificación one-hot y escalado, ajustados con train. |
| `red_neuronal.keras` | La red neuronal entrenada. |
| `umbral.json` | El umbral de decisión elegido en validación. |
| `ejemplo.csv` | Mediciones de todas las ciudades del 23/06/2017, para probar. |

Los tres archivos del modelo se generan al ejecutar la sección 9 del notebook.

## Entrada y salida

- **Entrada:** un CSV con las mediciones del día y las mismas columnas que el dataset original (`Date`, `Location`, `MinTemp`, `MaxTemp`, ...). Los valores faltantes se completan con lo aprendido en train.
- **Salida:** el mismo CSV con dos columnas nuevas: `probabilidad_lluvia` y `llueve_manana` (`Yes` o `No`).

## Armar la imagen

Desde esta carpeta (`docker/`):

```bash
docker build -t lluvia-australia .
```

## Correr la predicción

En PowerShell (Windows):

```powershell
docker run --rm -v "${PWD}:/datos" lluvia-australia /datos/ejemplo.csv /datos/predicciones.csv
```

En Linux o macOS:

```bash
docker run --rm -v "$(pwd):/datos" lluvia-australia /datos/ejemplo.csv /datos/predicciones.csv
```

- `--rm` borra el contenedor al terminar.
- `-v ...:/datos` monta la carpeta actual dentro del contenedor como `/datos`.
- Los dos últimos argumentos son el CSV de entrada y el de salida. El resultado queda en `predicciones.csv`, en la carpeta actual.

Para predecir otro día, se reemplaza `ejemplo.csv` por el archivo con las mediciones de ese día.

Al arrancar, TensorFlow imprime un par de líneas informativas (`oneDNN custom operations are on...`). No son errores: la predicción termina con el mensaje `49 predicciones guardadas en ...`.
