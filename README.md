# Trabajos Prácticos — Aprendizaje Automático 1

Tecnicatura en Inteligencia Artificial
Facultad de Ciencias Exactas, Ingeniería y Agrimensura — Universidad Nacional de Rosario

## Integrantes

- Aiup, Agustín
- Paoloni, Franco
- Silva, Julián

## Contenido

| | Trabajo | Notebook |
|---|---|---|
| **TP 1** | Regresión: predicción de precios de viviendas | [`TP_1/TP-regresion-AA1.ipynb`](TP_1/TP-regresion-AA1.ipynb) |
| **TP 2** | Clasificación: prediccion de lluvia en Australia  | [`TP_2/TP-clasificacion-AA1.ipynb`](TP_2/TP-clasificacion-AA1.ipynb) |

## Estructura del repositorio

```
TP_AA1_Aiup_Paoloni_Silva/
├── TP_1/
│   └── TP-regresion-AA1.ipynb          # notebook TP de regresión
|   └── TP-regresion-AA1-v2.ipynb       # notebook TP de regresión v2
├── data/
│   └── house-prices-tp.csv             # conjunto de datos regresión
|   └── weatherAUS_2026C2.csv           # conjunto de datos clasificación
├── docs/
│   └── TP_AA1_TP_Clasificacion.pdf     # consigna TP regresión
|   └── TP_AA1_TP_Regresion.pdf         # consigna TP clasificacion
└── requirements.txt                    # dependencias
```

## Cómo ejecutar

Desarrollado sobre Python 3.14.

```bash
python -m venv .venv
.venv\Scripts\activate          # en Linux o macOS: source .venv/bin/activate
pip install -r requirements.txt
```

Los notebooks leen el conjunto de datos con una ruta relativa (`../data/`), de modo que deben ejecutarse **desde su propia carpeta** (`TP_1/`, `TP_2/`).
