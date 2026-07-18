# **Proyecto de Clasificación de Cáncer de Mama**

### *Taller: GitHub para Control y Organización de Proyectos*

> Este proyecto forma parte del taller **"GitHub para Control y Organización de Proyectos"**, donde se aprenderá a estructurar, documentar y versionar un proyecto de Ciencia de Datos utilizando Git y GitHub de forma profesional.

---

## **Descripción general:**

El objetivo técnico del proyecto es entrenar un modelo de Machine Learning que clasifique tumores mamarios en dos categorías:

- M = Maligno
- B = Benigno

El objetivo pedagógico es que los estudiantes practiquen:

- El uso de Git y GitHub en un proyecto real.
- El diseño de una estructura profesional de carpetas para Ciencia de Datos.
- Cómo documentar proyectos usando Markdown.
- Cómo separar notebooks de scripts reutilizables (carpeta src).
- Cómo trabajar con Issues, ramas y Pull Requests.


## Estructura del proyecto:
```
proyecto-clasificacion-cancer-mama
|
|-- data/
|   |-- raw → Datos originales (CSV crudo)
|   |-- processed → Datos limpios generados por código
notebooks → Notebooks de exploración y entrenamiento
src → Scripts del proyecto: cargar datos, limpiar datos, entrenar modelo
.gitignore → Archivos que no se subirán a GitHub
README.md → Archivo de documentación principal
```

## **Dataset:**

Se utiliza un dataset de cáncer de mama (Breast Cancer Dataset). Contiene mediciones numéricas extraídas de imágenes de tumores y la columna de diagnóstico.

Columnas principales:

|Columna|Tipo|Descripción|
|-------|----|-----------|
id | Entero | identificador del registro (se elimina)
diagnosis | Categórica | M para maligno, B para benigno
radius_mean | Numérica | radio promedio
texture_mean | Numérica | textura promedio
perimeter_mean | Numérica | perímetro promedio
area_mean | Numérica | área promedio
Unnamed: 32 | Nula | columna vacía que se elimina en la limpieza

Durante la limpieza se crea una columna nueva llamada diagnosis_binaria, donde 1 representa maligno y 0 representa benigno.


## **Instalación y ejecución:**

### 1. Clonar el repositorio:
- git clone https://github.com/zetaware/proyecto-clasificacion-cancer-mama.git
- cd proyecto-clasificacion-cancer-mama

### 2. Instalar dependencias:
- pip install -r requirements.txt

### 3. Ejecutar el pipeline desde el notebook:
- Abrir el notebook llamado entrenamiento.ipynb en la carpeta notebooks y ejecutar las celdas correspondientes.

Resultados esperados:
- Un archivo limpio en data/processed con el nombre cancer_mama_procesado.csv
- Un modelo entrenado guardado en models/modelo_logistico.pkl
- Métricas impresas dentro del notebook (matriz de confusión y clasificación)


## **Checklist de tareas del taller:**

- [ ] Crear un repositorio en GitHub
- [ ] Clonar el repositorio en local
- [ ] Crear la estructura de carpetas del proyecto
- [ ] Agregar el dataset a data/raw
- [ ] Crear los scripts en src
- [ ] Crear y ejecutar los notebooks
- [ ] Hacer commits con mensajes claros
- [ ] Hacer push al repositorio remoto
- [ ] Crear Issues para mejoras
- [ ] Crear ramas y Pull Requests
- [ ] Mejorar la documentación con ejemplos


Herramientas utilizadas:

Lenguaje: Python 3
Librerías: pandas, numpy, scikit-learn, matplotlib, seaborn, joblib
Entorno: Jupyter Notebooks, VS Code
Control de versiones: Git y GitHub


Enlaces útiles:

Documentación oficial de Git: https://git-scm.com/doc
GitHub Docs: https://docs.github.com/es
Documentación de Scikit-learn: https://scikit-learn.org/stable/
Guía básica de Markdown: https://www.markdownguide.org/basic-syntax/


Valentin Guerrero
Grow Up
Prueba de una Nueva Rama
