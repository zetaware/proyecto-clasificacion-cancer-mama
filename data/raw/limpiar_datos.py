from pathlib import Path
import pandas as pd


def preparar_datos(df):
    """
    Limpieza básica del dataset:

    - Elimina la columna 'id' si existe.
    - Elimina columnas completamente vacías (como 'Unnamed: 32').
    - Elimina filas duplicadas.
    - Crea una columna 'diagnosis_binaria' (M=1, B=0).
    - Rellena valores faltantes numéricos con la mediana.
    """
    df_limpio = df.copy()

    # 1) Eliminar columna 'id' si está presente
    if "id" in df_limpio.columns:
        df_limpio = df_limpio.drop(columns=["id"])

    # 2) Eliminar columnas completamente vacías
    columnas_vacias = [c for c in df_limpio.columns if df_limpio[c].isna().all()]
    if columnas_vacias:
        print("🧹 Eliminando columnas vacías:", columnas_vacias)
        df_limpio = df_limpio.drop(columns=columnas_vacias)

    # 3) Eliminar filas duplicadas
    df_limpio = df_limpio.drop_duplicates()

    # 4) Crear columna binaria para diagnóstico
    df_limpio["diagnosis_binaria"] = df_limpio["diagnosis"].map({"M": 1, "B": 0})

    # 5) Rellenar valores faltantes en columnas numéricas con la mediana
    columnas_numericas = df_limpio.select_dtypes(include=["int64", "float64"]).columns
    n_nulos_antes = df_limpio[columnas_numericas].isna().sum().sum()

    df_limpio[columnas_numericas] = df_limpio[columnas_numericas].fillna(
        df_limpio[columnas_numericas].median()
    )

    n_nulos_despues = df_limpio[columnas_numericas].isna().sum().sum()

    print("NaN numéricos antes:", n_nulos_antes)
    print("NaN numéricos después:", n_nulos_despues)

    return df_limpio


def guardar_datos_procesados(df_limpio, nombre_archivo="cancer_mama_procesado.csv"):
    """
    Guarda el DataFrame limpio en la carpeta data/processed.

    Parámetros:
        df_limpio (DataFrame): datos ya preparados.
        nombre_archivo (str): nombre del archivo CSV de salida.
    """
    raiz = Path(__file__).resolve().parents[1]
    ruta_salida = raiz / "data" / "processed" / nombre_archivo

    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    df_limpio.to_csv(ruta_salida, index=False)

    print(f"Datos procesados guardados en: {ruta_salida}")


if __name__ == "__main__":
    from cargar_datos import cargar_datos

    df_original = cargar_datos()
    df_limpio = preparar_datos(df_original)
    guardar_datos_procesados(df_limpio)

    print("Datos preparados y guardados")
