import pandas as pd

# --- Parte 1: Series ---

# Ejercicio 1
cursos = pd.Series([30, 25, 28, 32], index=["3A", "3B", "4A", "4B"])
print("Alumnos del primer curso:", cursos.iloc[0])

# Ejercicio 2
notas = pd.Series([8, 6, 9, 7, 10], index=["Matemática", "Lengua", "Historia", "Geografía", "Inglés"])
print("Nota de Matemática:", notas["Matemática"])

# Ejercicio 3
productos1 = pd.Series([100, 200, 150], index=["Pan", "Leche", "Huevos"])
productos2 = pd.Series([90, 200, 80], index=["Pan", "Leche", "Queso"])
print("Suma de Series:")
print(productos1 + productos2)

# Ejercicio 4
temperaturas = pd.Series([20, 22, 25, 18, 21, 19, 23])
print("Temperatura máxima:", temperaturas.max())

# Ejercicio 5
profesores = pd.Series([10, 5, 15], index=["Ana", "Luis", "Marta"])
print("Promedio de antigüedad:", profesores.mean())

# --- Parte 2: DataFrames ---

# Ejercicio 1
alumnos = pd.DataFrame({
    "Alumno": ["Ana", "Juan", "Pedro"],
    "Curso": ["6A", "6B", "6A"],
    "Nota": [8, 6, 9]
})
print("Columna de cursos:")
print(alumnos["Curso"])

# Ejercicio 2
productos = pd.DataFrame({
    "Producto": ["Pan", "Leche", "Queso", "Huevos"],
    "Precio": [100, 200, 300, 150]
})
productos["IVA"] = productos["Precio"] * 0.21
print(productos)

# Ejercicio 3
ciudades = pd.DataFrame({
    "Ciudad": ["Ciudad A", "Ciudad B", "Ciudad C", "Ciudad D", "Ciudad E"],
    "Poblacion": [50000, 150000, 200000, 80000, 120000]
})
print("Ciudades con más de 100.000 habitantes:")
print(ciudades[ciudades["Poblacion"] > 100000])

# Ejercicio 4
materias = pd.DataFrame({
    "Materia": ["Matemática", "Lengua", "Historia", "Geografía", "Inglés"],
    "Nota": [8, 5, 6, 7, 9]
})
print("Materias aprobadas:")
print(materias[materias["Nota"] >= 6])

# Ejercicio 5
jugadores = pd.DataFrame({
    "Nombre": ["Luis", "Ana", "Pedro", "Juan"],
    "Posición": ["Delantero", "Mediocampo", "Defensa", "Delantero"],
    "Goles": [10, 4, 2, 7]
})
print("Total de goles:", jugadores["Goles"].sum())
