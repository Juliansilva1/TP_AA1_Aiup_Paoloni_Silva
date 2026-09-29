# Trabajos Prácticos — Aprendizaje Automático 1

Tecnicatura en Inteligencia Artificial
Facultad de Ciencias Exactas, Ingeniería y Agrimensura — Universidad Nacional de Rosario

## Integrantes

- Aiup, Agustín
- Paoloni, Franco
- Silva, Julián

## Contenido

| | Trabajo | Notebook | Estado |
|---|---|---|---|
| **TP 1** | Regresión: predicción de precios de viviendas | [`TP_1/TP-regresion-AA1.ipynb`](TP_1/TP-regresion-AA1.ipynb) | Entregado |
| **TP 2** | Clasificación | `TP_2/TP-clasificacion-AA1.ipynb` | Pendiente |

### TP 1 — Predicción de precios de viviendas

Se predice el valor mediano de viviendas de Boston (`MEDV`, en miles de dólares) a partir de 13 variables que describen cada barrio, mediante **regresión lineal múltiple**.

El trabajo recorre el análisis descriptivo del conjunto de datos (tratamiento de valores faltantes, detección de atípicos, matriz de correlación, escalado y partición en entrenamiento y prueba) y luego compara siete formas de resolver el mismo problema:

- Regresión lineal por **mínimos cuadrados**.
- **Descenso por el gradiente** en sus tres variantes: por lotes, estocástico y mini-batch, calculado con las funciones provistas por la cátedra.
- **Regularización**: Ridge, Lasso y ElasticNet, con sus hiperparámetros elegidos por validación cruzada.

## Estructura del repositorio

```
TP_AA1_Aiup_Paoloni_Silva/
├── TP_1/
│   └── TP-regresion-AA1.ipynb    # notebook del TP de regresión
├── data/
│   └── house-prices-tp.csv       # conjunto de datos
├── docs/
│   └── TP_AA1_Consigna.pdf       # consigna de la cátedra
└── requirements.txt              # dependencias
```

## Cómo ejecutar

Desarrollado sobre Python 3.14.

```bash
python -m venv .venv
.venv\Scripts\activate          # en Linux o macOS: source .venv/bin/activate
pip install -r requirements.txt
```

Los notebooks leen el conjunto de datos con una ruta relativa (`../data/`), de modo que deben ejecutarse **desde su propia carpeta** (`TP_1/`, `TP_2/`).
