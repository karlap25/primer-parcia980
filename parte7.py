import sqlite3

conexion = sqlite3.connect("organizador_viajes.db")

create_table_query = """
CREATE TABLE IF NOT EXISTS viajes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    presupuesto REAL,
    hospedaje TEXT,
    boletos_avion TEXT,
    comida REAL,
    fecha_inicio TEXT,
    fecha_fin TEXT,
    pais TEXT
)
"""

conexion.execute(create_table_query)

def display_menu():
    print("1. Agregar viaje")
    print("2. Ver historial de viajes")
    print("3. Salir")

def agregar_viaje():
    presupuesto = float(input("Ingrese el presupuesto del viaje: "))
    hospedaje = input("Ingrese el tipo de hospedaje: ")
    boletos_avion = input("Ingrese los detalles de los boletos de avión: ")
    comida = float(input("Ingrese el presupuesto para comida durante el viaje: "))
    fecha_inicio = input("Ingrese la fecha de inicio del viaje (YYYY-MM-DD): ")
    fecha_fin = input("Ingrese la fecha de fin del viaje (YYYY-MM-DD): ")
    pais = input("Ingrese el nombre del país a visitar: ")

    conexion.execute("INSERT INTO viajes (presupuesto, hospedaje, boletos_avion, comida, fecha_inicio, fecha_fin, pais) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                     (presupuesto, hospedaje, boletos_avion, comida, fecha_inicio, fecha_fin, pais))
    conexion.commit()
    print("Viaje agregado exitosamente.")

def ver_historial_viajes():
    cursor = conexion.execute("SELECT * FROM viajes")
    viajes = cursor.fetchall()
    if viajes:
        print("Historial de viajes:")
        for viaje in viajes:
            print(f"ID: {viaje[0]}, Presupuesto: {viaje[1]}, Hospedaje: {viaje[2]}, Boletos de avión: {viaje[3]}, Comida: {viaje[4]}, Fecha de inicio: {viaje[5]}, Fecha de fin: {viaje[6]}, País: {viaje[7]}")
    else:
        print("No hay viajes registrados en el historial.")

def main():
    while True:
        display_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_viaje()
        elif opcion == "2":
            ver_historial_viajes()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
