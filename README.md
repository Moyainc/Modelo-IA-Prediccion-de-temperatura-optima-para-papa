# Predicción de la Temperatura Óptima para el Cultivo de Papa en Colombia

## Descripción

Este proyecto de investigación aplica técnicas de **Machine Learning** para estimar la temperatura óptima para el cultivo de papa en Colombia a partir de datos climáticos y agrícolas obtenidos de fuentes oficiales.

El objetivo principal es analizar la relación entre variables ambientales y las condiciones adecuadas para el cultivo de papa, utilizando modelos de aprendizaje automático para generar predicciones precisas.

El proyecto incluye:

- Análisis exploratorio de datos
- Entrenamiento y comparación de múltiples modelos de Machine Learning
- Optimización de hiperparámetros
- Selección del modelo con mejor desempeño
- Implementación de una API para realizar predicciones

# Metodología

El proyecto fue desarrollado siguiendo las siguientes etapas:

1. **Recolección de datos**
   - Obtención de datasets provenientes de bases de datos oficiales de Colombia.

2. **Preprocesamiento de datos**
   - Limpieza de datos
   - Análisis exploratorio
   - Selección de variables relevantes

3. **Entrenamiento de modelos**
   - Evaluación de diferentes algoritmos de Machine Learning.

4. **Optimización de hiperparámetros**
   - Búsqueda de los mejores parámetros para mejorar el rendimiento del modelo.

5. **Evaluación**
   - Comparación de modelos mediante métricas estadísticas.

6. **Implementación**
   - Integración del modelo mediante una API desarrollada con FastAPI.

# Modelo seleccionado

El modelo con mejor desempeño fue **K-Nearest Neighbors (KNN)** después del proceso de optimización de hiperparámetros.

## Mejores hiperparámetros encontrados
n_neighbors = 3
p = 1
weights = distance
# Resultados del modelo

Las métricas obtenidas durante la evaluación fueron:
**Error cuadrático medio (MSE)** 0.0867
**Coeficiente de determinación (R²)** 0.9912
**Validación cruzada (10-fold)** R² promedio: 0.9916 ± 0.0062
Estos resultados indican que el modelo presenta una **alta capacidad de predicción y generalización** sobre los datos analizados.

# Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- FastAPI
- Uvicorn
- Jupyter Notebook

# Estructura del proyecto

data/ -> Datasets utilizados
notebooks/ -> Análisis exploratorio y entrenamiento del modelo
models/ -> Modelo entrenado
api/ -> Implementación de la API
requirements.txt
README.md

# Instalación del proyecto

Clonar el repositorio:
git clone https://github.com/TU-USUARIO/TU-REPOSITORIO.git
Entrar al directorio del proyecto:
cd TU-REPOSITORIO
Instalar dependencias:
pip install -r requirements.txt

# Ejecutar la API
Para iniciar el servidor de la API:
uvicorn main:app --reload
Luego la API estará disponible en:
http://127.0.0.1:8000

# Uso del modelo

La API permite enviar datos de entrada y obtener como respuesta la predicción de la **temperatura óptima estimada por el modelo entrenado**.

# Autor

**Andrés Moya Perea**  
Ingeniero de Sistemas
