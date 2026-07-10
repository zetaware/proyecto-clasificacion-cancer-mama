from pathlib import Path
import pandas as pd


def cargar_datos():
    """
    Carga el dataset de cáncer de mama desde la carpeta data/raw.

    Devuelve:
        df (DataFrame): datos cargados en memoria.
    """
    # Ruta raíz del proyecto
    raiz = Path(__file__).resolve().parents[1]
    ruta_csv = raiz / "data" / "raw" / "cancer_mama.csv"

    df = pd.read_csv(ruta_csv)

    print("Datos cargados")
    print("Filas:", df.shape[0], " Columnas:", df.shape[1])

    return df


if __name__ == "__main__":
    # Prueba rápida
    df = cargar_datos()
    print(df.head())
