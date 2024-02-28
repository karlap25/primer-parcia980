import sys
from os import system
import sqlite3

conexion = sqlite3.connect("proyectos.db")

create_table_query = """
CREATE TABLE IF NOT EXISTS tareas (
    user TEXT,
    libro TEXT,
    finalizado BOOLEAN
)
"""

conexion.execute(create_table_query)

def login():
    usuario = input("Usuario: ")
    # Add logic to verify credentials
    return usuario  # Return username for now

def display_menu():
    print("1. Ingresar tarea nueva")
    print("2. Visualizar tareas registradas")
    print("3. Salir")

def programa_2(user_name):
    system('cls')
    print("Tareas")
    print("1. Agregar tarea")
    print("2. Visualizar tareas")
    optdict = {"si": 1, "no": 0}
    
    option = int(input("Que operacion desea realizar?"))
    while option not in {1, 2}:
        option = int(input("Ingrese una opcion valida"))
    
    if option == 1:
        tarea_name = input("Ingrese tarea: ")
        finished = input("Ya finalizo esta tarea? Si o No?")
        while finished.lower() not in {"si", "no"}:
            finished = input("Por favor responda. Si o No.")
        conexion.execute("INSERT INTO tareas(user, libro, finalizado) VALUES (?, ?, ?)", (user_name, tarea_name, optdict.get(finished.lower(), 0)))
        conexion.commit()
    elif option == 2:
        cursor = conexion.execute(f"SELECT user, libro, finalizado FROM tareas WHERE user = '{user_name}'")
        for fila in cursor:
            print(f"Usuario: {fila[0]}, Tarea: {fila[1]}, Finalizada: {'Si' if fila[2] == 1 else 'No'}")
    
    input("Presione Enter para Continuar\n")
    system('cls')

def main():
    user_name = login()
    if user_name:
        while True:
            display_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                programa_2(user_name)
            elif opcion == "2":
                 cursor = conexion.execute(f"SELECT user, libro, finalizado FROM tareas WHERE user = '{user_name}'")
                 for fila in cursor:
                     print(f"Usuario: {fila[0]}, Tarea: {fila[1]}, Finalizado: {'Si' if fila[2] == 1 else 'No'}")
            elif opcion == "3":
                break
            else:
                print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()

