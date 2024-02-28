import sqlite3

conexion = sqlite3.connect("proyectos.db")

create_table_query = """
CREATE TABLE IF NOT EXISTS ejercicio (
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
    print("1. Registrar ejercicio")
    print("2. Salir")

def programa_2(user_name):
    print("Ejercicio")
    print("1. Agregar ejercicio")
    print("2. Visualizar ejercicios realizados")
    print("3. Eliminar ejercicio")

    option = input("¿Qué operación desea realizar? ")
    while option not in {"1", "2", "3"}:
        option = input("Ingrese una opción válida: ")

    if option == "1":
        tarea_name = input("Ingrese ejercicio y fecha de entrenamiento: ")
        conexion.execute("INSERT INTO ejercicio (user, libro, finalizado) VALUES (?, ?, ?)", (user_name, tarea_name, False))
        conexion.commit()
    elif option == "2":
        cursor = conexion.execute("SELECT user, libro, finalizado FROM ejercicio WHERE user = ?", (user_name,))
        for fila in cursor:
            print(f"Usuario: {fila[0]}, Ejercicio realizado: {fila[1]}")
    elif option == "3":
        ejercicio_id = input("Ingrese el ID del ejercicio que desea eliminar: ")
        try:
            conexion.execute("DELETE FROM ejercicio WHERE rowid = ? AND user = ?", (ejercicio_id, user_name))
            conexion.commit()
            print("Ejercicio eliminado exitosamente.")
        except:
            print("Error al eliminar el ejercicio.")

    input("Presione Enter para Continuar\n")


def main():
    user_name = login()
    if user_name:
        while True:
            display_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                programa_2(user_name)
            elif opcion == "2":
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
