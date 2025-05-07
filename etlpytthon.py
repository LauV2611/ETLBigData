import pandas as pd

# EXTRACT
df = pd.read_csv("Hate_Crimes_2017-2025.csv")

# TRANSFORM
def transform_data(df):
    # Eliminar filas con valores vacíos
    df = df.dropna()

    # Convertir nombres de columnas a minúsculas
    df.columns = [col.lower().strip() for col in df.columns]

    # Formatear fechas si existe una columna de fecha
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

    return df

print("Antes:")
print(df.head())

# LOAD
df_transformado = transform_data(df)

print("Después:")
print(df_transformado.head())

# Guardar en un nuevo CSV
df_transformado.to_csv("hate_crimes_limpio.csv", index=False)
