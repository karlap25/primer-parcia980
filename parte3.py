import sqlite3

conexion = sqlite3.connect("proyectos.db")

create_table_query = """
CREATE TABLE IF NOT EXISTS consumo_agua (
    fecha TEXT,
    cantidad_ml INTEGER
)
"""

conexion.execute(create_table_query)

def login():
    usuario = input("Usuario: ")
    # Aquí podrías implementar la lógica para verificar credenciales si lo necesitas
    return usuario

def display_menu():
    print("1. Registrar consumo diario de agua")
    print("2. Ver promedio semanal de consumo de agua")
    print("3. Salir")

def registrar_consumo_agua():
    fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
    cantidad_ml = int(input("Ingrese la cantidad de agua consumida en mililitros: "))
    conexion.execute("INSERT INTO consumo_agua (fecha, cantidad_ml) VALUES (?, ?)", (fecha, cantidad_ml))
    conexion.commit()

def promedio_semanal_consumo_agua():
    cursor = conexion.execute("SELECT cantidad_ml FROM consumo_agua WHERE date(fecha) BETWEEN date('now', '-6 days') AND date('now')")
    consumos_semanales = [fila[0] for fila in cursor]
    if consumos_semanales:
        promedio_semanal = sum(consumos_semanales) / len(consumos_semanales)
        print(f"El promedio semanal de consumo de agua es: {promedio_semanal} ml")
    else:
        print("No hay datos suficientes para calcular el promedio semanal.")

def main():
    usuario = login()
    if usuario:
        while True:
            display_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                registrar_consumo_agua()
            elif opcion == "2":
                promedio_semanal_consumo_agua()
            elif opcion == "3":
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
