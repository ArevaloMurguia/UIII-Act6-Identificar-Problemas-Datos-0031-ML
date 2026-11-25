
# =====================================================
# PRACTICA: IDENTIFICACION DE PROBLEMAS EN LOS DATOS
# CASO 1: TITANIC
# Machine Learning - Data Cleaning
# =====================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Rafael Arevalo - NC 0031

print("======================================")
print(" ANALISIS DEL DATASET TITANIC")
print("======================================")

# Crear carpeta de resultados
os.makedirs("caso1-titanic/resultados", exist_ok=True)

# 1. Cargar dataset
df = pd.read_csv("caso1-titanic/datos/titanic.csv")

print("\n1. VISTA PREVIA DE LOS DATOS")
print(df.head())

# 2. Dimensiones
print("\n2. DIMENSIONES")
print("Filas:", df.shape[0])
print("Columnas:", df.shape[1])

# 3. Tipos de datos
print("\n3. TIPOS DE DATOS")
print(df.dtypes)

# 4. Datos nulos
print("\n4. DATOS NULOS")
nulos = df.isnull().sum()
print(nulos[nulos > 0])

# 5. Porcentaje de nulos
print("\n5. PORCENTAJE DE DATOS NULOS")
porcentaje = (df.isnull().mean() * 100).round(2)
print(porcentaje[porcentaje > 0])

# 6. Registros duplicados
print("\n6. REGISTROS DUPLICADOS")
print("Duplicados:", df.duplicated().sum())

# 7. Valores atipicos en la edad
print("\n7. VALORES ATIPICOS EN AGE")

Q1 = df["age"].quantile(0.25)
Q3 = df["age"].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

atipicos = df[
    (df["age"] < limite_inferior) |
    (df["age"] > limite_superior)
]

print("Valores atipicos encontrados:", len(atipicos))

# 8. Grafica de datos nulos
plt.figure(figsize=(10, 5))

sns.heatmap(
    df.isnull(),
    cbar=False,
    cmap="viridis",
    yticklabels=False
)

plt.title("Datos faltantes del Titanic")
plt.tight_layout()
plt.savefig("caso1-titanic/resultados/nulos_titanic.png")
plt.close()

print("\nGrafica guardada correctamente.")

# 9. Limpieza de datos
df_limpio = df.copy()

# Eliminar duplicados
df_limpio = df_limpio.drop_duplicates()

# Rellenar edades con la mediana
mediana = df_limpio["age"].median()
df_limpio["age"] = df_limpio["age"].fillna(mediana)

# Rellenar ciudad de embarque con la moda
moda = df_limpio["embark_town"].mode()[0]
df_limpio["embark_town"] = (
    df_limpio["embark_town"].fillna(moda)
)

# 10. Guardar datos limpios
df_limpio.to_csv(
    "caso1-titanic/resultados/titanic_limpio.csv",
    index=False
)

print("\n10. RESULTADOS FINALES")
print("Filas originales:", len(df))
print("Filas limpias:", len(df_limpio))
print("Nulos restantes:")
print(df_limpio.isnull().sum())

print("\n======================================")
print(" ANALISIS COMPLETADO CORRECTAMENTE")
print("======================================")


print("*-*-*- Arevalo Rafael NC:0031 *-*-*-*-")