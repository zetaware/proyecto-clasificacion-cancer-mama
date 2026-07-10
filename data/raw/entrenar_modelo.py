from pathlib import Path
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix


def entrenar_modelo(df):
    """
    Entrena una Regresión Logística para predecir diagnosis_binaria
    usando solo un subconjunto de columnas (las columnas 1 a 11).
    """
    # Seleccionar solo algunas columnas como features
    # df.columns[0]  -> diagnosis
    # df.columns[1:11] -> columnas numéricas seleccionadas
    feature_cols = list(df.columns[1:11])
    print("📌 Usando estas columnas como features:")
    print(feature_cols)

    X = df[feature_cols]
    y = df["diagnosis_binaria"]

    # Train / Test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Pipeline: escalador + modelo
    pipeline = Pipeline(
        steps=[
            ("escalador", StandardScaler()),
            ("modelo", LogisticRegression(max_iter=1000)),
        ]
    )

    # Entrenar
    pipeline.fit(X_train, y_train)

    # Predicciones
    y_pred = pipeline.predict(X_test)

    # Métricas
    print("Matriz de confusión:")
    print(confusion_matrix(y_test, y_pred))
    print("\nReporte de clasificación:")
    print(classification_report(y_test, y_pred))

    return pipeline


def guardar_modelo(pipeline):
    """
    Guarda el modelo entrenado en la carpeta models.
    """
    raiz = Path(__file__).resolve().parents[1]
    ruta_modelo = raiz / "models" / "modelo_logistico.pkl"

    ruta_modelo.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, ruta_modelo)

    print(f"Modelo guardado en: {ruta_modelo}")


if __name__ == "__main__":
    from cargar_datos import cargar_datos
    from limpiar_datos import preparar_datos

    df_original = cargar_datos()
    df_limpio = preparar_datos(df_original)

    modelo = entrenar_modelo(df_limpio)
    guardar_modelo(modelo)
