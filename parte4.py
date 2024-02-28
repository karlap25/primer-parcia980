import sys
from os import system
import sqlite3

conexion = sqlite3.connect("proyectos.db")

# Crear tablas de los distintos programas
try:
    conexion.execute("""
        CREATE TABLE IF NOT EXISTS habitos_lectura (
                     user text,
                     libro text,
                     finalizado boolean
        )
    """)
except sqlite3.OperationalError:
    print("Error con la base de datos.")

def rename(newname):
    def decorator(f):
        f.__name__ = newname
        return f
    return decorator


def display_menu(menu):
    """
    Display a menu where the key identifies the name of a function.
    :param menu: dictionary, key identifies a value which is a function name
    :return:
    """
    for k, function in menu.items():
        print(k, function.__name__)


@rename("Control de habitos de lectura")
def programa_4(user_name):
    system('cls')
    print("Control de habitos de lectura")
    print("1. Agregar un libro")
    print("2. Visualizar datos")
    optdict = {
        "si": 1,
        "no": 0
    }
    option = int(input("Que operacion desea realizar?"))
    while option not in {1, 2}:
        option = int(input("Ingrese una opcion valida"))
    if option == 1:
        book_name = input("Ingrese nombre del libro: ")
        finished = input("Ya finalizo este libro? Si o No?")
        while finished.lower() not in {"si", "no"}:
            finished = input("Por favor responda. Si o No.")
        conexion.execute("INSERT INTO habitos_lectura(user, libro, finalizado) VALUES (?, ?, ?)", (user_name, book_name, optdict[finished.lower()]))
        conexion.commit()
    elif option == 2:
        cursor = conexion.execute(f"SELECT user, libro, finalizado FROM habitos_lectura WHERE user = '{user_name}'")
        for fila in cursor:
            print(f"Usuario: {fila[0]}, Libro: {fila[1]}, Finalizado: {'Si' if fila[2] == 1 else 'No'}")
    
    input("Press Enter to Continue\n")
    system('cls')  # clears stdout


@rename("Salir")
def exit(user_name):
    system('cls')  # clears stdout
    print("Goodbye")
    sys.exit()


def main():
    user_name = input("Usuario: ")
    print(f"Bienvenido, {user_name}")
    functions_names = [
                       programa_4, 
                       
                       exit]
    menu_items = dict(enumerate(functions_names, start=1))

    while True: 
        try:
            display_menu(menu_items)
            selection = int(
                input("Seleccione un programa: "))
            selected_value = menu_items[selection]
            selected_value(user_name)
        except Exception as e:
            system('cls')
            print('Opcion invalida, intente de nuevo!')
            print(e)
            


if __name__ == "__main__":
    main()
    