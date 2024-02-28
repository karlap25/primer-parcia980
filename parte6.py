import sqlite3

conexion = sqlite3.connect("proyectos.db")

create_table_query = """
CREATE TABLE IF NOT EXISTS proyectos (
    nombre TEXT,
    estado TEXT
)
"""

conexion.execute(create_table_query)

def login():
    usuario = input("Usuario: ")
    # Aquí podrías implementar la lógica para verificar credenciales si lo necesitas
    return usuario

def display_menu():
    print("1. Agregar proyecto")
    print("2. Editar estado de proyecto")
    print("3. Borrar proyecto")
    print("4. Proyectos abiertos")
    print("5. Salir")

def agregar_proyecto():
    nombre = input("Ingrese el nombre del proyecto: ")
    estado = "abierto"  # Por defecto, un proyecto nuevo se considera abierto
    conexion.execute("INSERT INTO proyectos (nombre, estado) VALUES (?, ?)", (nombre, estado))
    conexion.commit()
    print("Proyecto agregado exitosamente.")

def editar_estado_proyecto():
    nombre = input("Ingrese el nombre del proyecto a editar: ")
    nuevo_estado = input("Ingrese el nuevo estado del proyecto (abierto/cerrado): ")
    conexion.execute("UPDATE proyectos SET estado = ? WHERE nombre = ?", (nuevo_estado, nombre))
    conexion.commit()
    print("Estado del proyecto actualizado correctamente.")

def borrar_proyecto():
    nombre = input("Ingrese el nombre del proyecto a borrar: ")
    conexion.execute("DELETE FROM proyectos WHERE nombre = ?", (nombre,))
    conexion.commit()
    print("Proyecto borrado correctamente.")

def proyectos_abiertos():
    cursor = conexion.execute("SELECT nombre, estado FROM proyectos WHERE estado = 'abierto'")
    proyectos = cursor.fetchall()
    if proyectos:
        print("Proyectos abiertos:")
        for proyecto in proyectos:
            print(f"Nombre: {proyecto[0]}, Estado: {proyecto[1]}")
    else:
        print("No hay proyectos abiertos en este momento.")

def main():
    usuario = login()
    if usuario:
        while True:
            display_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                agregar_proyecto()
            elif opcion == "2":
                editar_estado_proyecto()
            elif opcion == "3":
                borrar_proyecto()
            elif opcion == "4":
                proyectos_abiertos()
            elif opcion == "5":
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
