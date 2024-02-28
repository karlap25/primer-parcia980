import json
import os
from collections import defaultdict

# Función para solicitar usuario y contraseña
def login():
    username = input("Usuario: ")
    
    # Verificar si el usuario y contraseña son correctos (esto puede ser más robusto en un programa real)
    if username == "karla":
        return True
    else:
        print("Credencia incorrecto.")
        return False

# Función para cargar los datos del archivo JSON
def cargar_datos():
    if os.path.exists("datos_alimenticios.json"):
        with open("datos_alimenticios.json", "r") as file:
            return json.load(file)
    else:
        return {"gastos_alimentos": [], "metas_nutricionales": {}}

# Función para guardar los datos en el archivo JSON
def guardar_datos(datos):
    with open("datos_alimenticios.json", "w") as file:
        json.dump(datos, file)

# Función para registrar un gasto en alimentos
def registrar_gasto(datos):
    nombre = input("Ingrese el tipo de alimento: ")
    costo = float(input("Ingrese el costo del alimento: "))
    categoria = input("Ingrese la categoría del alimento (ej. Proteínas, Frutas y Verduras, Golosina, Bebidas.): ")
    datos["gastos_alimentos"].append({"nombre": nombre, "costo": costo, "categoria": categoria})
    print("Gasto registrado exitosamente.")

# Función para obtener análisis de hábitos alimenticios
def obtener_analisis(datos):
    categorias = defaultdict(float)
    for gasto in datos["gastos_alimentos"]:
        categorias[gasto["categoria"]] += gasto["costo"]
    
    print("Análisis de hábitos alimenticios:")
    for categoria, gasto_total in categorias.items():
        print(f"- {categoria}: Q{gasto_total:.2f}")

# Función para ofrecer sugerencias de ajuste de presupuesto
def ofrecer_sugerencias(datos):
    pass  # En esta versión básica, esta función está vacía

# Función para establecer metas nutricionales
def establecer_metas_nutricionales(datos):
    objetivo = input("Ingrese una meta alimenticia: ")
    datos["metas_nutricionales"]["objetivo"] = objetivo
    print("Meta establecida exitosamente.")

# Función principal del programa
def main():
    # Solicitar login
    while not login():
        pass

    # Cargar datos
    datos = cargar_datos()

    # Menú principal
    while True:
        print("\nDatos Alimenticios")
        print("1. Registrar gasto en alimentos")
        print("2. Obtener análisis de hábitos alimenticios")
        print("4. Establecer metas nutricionales")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_gasto(datos)
        elif opcion == "2":
            obtener_analisis(datos)
        elif opcion == "3":
            ofrecer_sugerencias(datos)
        elif opcion == "4":
            establecer_metas_nutricionales(datos)
        elif opcion == "5":
            guardar_datos(datos)
            print("Recuerda comer lo más sano posible!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Iniciar programa
if __name__ == "__main__":
    main()
