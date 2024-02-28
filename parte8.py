import sqlite3

conexion = sqlite3.connect("proyectos.db")

create_table_query = """
CREATE TABLE IF NOT EXISTS horas_sueno (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT,
    horas INTEGER
)
"""

conexion.execute(create_table_query)

def display_menu():
    print("1. Registrar horas de sueño")
    print("2. Ver resumen de horas de sueño")
    print("3. Salir")

def registrar_horas_sueno():
    fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
    horas = float(input("Ingrese las horas de sueño: "))
    conexion.execute("INSERT INTO horas_sueno (fecha, horas) VALUES (?, ?)", (fecha, horas))
    conexion.commit()
    print("Horas de sueño registradas exitosamente.")

def ver_resumen_horas_sueno():
    cursor = conexion.execute("SELECT fecha, horas FROM horas_sueno")
    registros = cursor.fetchall()
    if registros:
        print("Resumen de horas de sueño:")
        total_horas = 0
        total_dias = 0
        for registro in registros:
            print(f"Fecha: {registro[0]}, Horas de sueño: {registro[1]}")
            total_horas += registro[1]
            total_dias += 1

        if total_dias >= 7:
            promedio_semanal = total_horas / 7
            print(f"Promedio de horas de sueño semanal: {promedio_semanal}")
    else:
        print("No hay registros de horas de sueño.")

def main():
    while True:
        display_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_horas_sueno()
        elif opcion == "2":
            ver_resumen_horas_sueno()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
