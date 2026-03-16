from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import numpy as np
import joblib

app = FastAPI()

# Cargar el modelo con manejo de errores
try:
    modelo = joblib.load("../Modelos/modelo_knn_temperatura.pkl")
except Exception as e:
    modelo = None
    print(f"Error al cargar el modelo: {e}")

# Clase de entrada (ahora incluye año y departamento)
class InputData(BaseModel):
    area_ha: float = Field(..., gt=0, description="Área en hectáreas")
    precipitacion: float = Field(..., ge=0, description="Precipitación en mm")
    altitud_mm: float = Field(..., ge=0, description="Altitud en metros")
    humedad_relativa: float = Field(..., ge=0, le=100, description="Humedad relativa (%)")
    radiacion_solar: float = Field(..., ge=0, description="Radiación solar (W/m2)")
    ano: int = Field(..., ge=2010, le=2023, description="Año (2010-2023)")
    departamento: str = Field(..., min_length=3, description="Departamento (ej: 'HUILA')")

@app.post("/predecir/")
def predecir_temperatura(data: InputData):
    if modelo is None:
        raise HTTPException(status_code=500, detail="Modelo no disponible")

    try:
        # Lista de columnas dummy necesarias para el modelo
        anios = [f"ano_{y}" for y in range(2010, 2024)]
        departamentos = [
            "ANTIOQUIA", "BOYACA", "CALDAS", "CASANARE", "CAUCA", "CHOCO",
            "CUNDINAMARCA", "HUILA", "META", "NARINO", "NORTE_DE_SANTANDER",
            "PUTUMAYO", "QUINDIO", "SANTANDER", "TOLIMA", "VALLE_DEL_CAUCA"
        ]

        # Diccionario base con los datos ingresados por el usuario
        entrada_dict = {
            "area_ha": data.area_ha,
            "precipitacion": data.precipitacion,
            "altitud_mm": data.altitud_mm,
            "humedad_relativa": data.humedad_relativa,
            "radiacion_solar": data.radiacion_solar
        }

        # Añadir columnas dummy de año (según el valor ingresado)
        for a in anios:
            entrada_dict[a] = 1 if a == f"ano_{data.ano}" else 0

        # Añadir columnas dummy de departamento (normalizado a mayúsculas y sin espacios)
        departamento_normalizado = data.departamento.upper().replace(" ", "_")
        for d in departamentos:
            col = f"departamento_{d}"
            entrada_dict[col] = 1 if d == departamento_normalizado else 0

        # Convertir a array ordenado para el modelo
        entrada_array = np.array([list(entrada_dict.values())])
        prediccion = modelo.predict(entrada_array)

        return {"temperatura_predicha": round(float(prediccion[0]), 2)}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error en la predicción: {str(e)}")

# Ejemplo de ruta GET para verificar que el API está funcionando
@app.get("/")
def read_root():
    return {"message": "API de predicción de temperatura activa"}