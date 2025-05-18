import sqlite3
from random import randint

# Conexión a la base de datos (se crea si no existe)
conn = sqlite3.connect("matriculas.db")
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS alumnos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    curso TEXT,
    sede TEXT,
    horario TEXT,
    codigo_pago TEXT
)
""")

# Lista para guardar en memoria también (opcional)
alumnos_matriculados = []

# Bucle principal
while True:
    print("\n--- MATRÍCULA WETALK CIBERTEC ---")

    # Entrada de datos
    nombre = input("Nombre del alumno: ").strip()
    estado = input("Estado del alumno (activo/inactivo): ").strip().lower()
    deuda = input("¿Tiene deuda pendiente? (sí/no): ").strip().lower()

    # Validación
    if estado == "activo" and deuda == "no":
        print("Alumno apto para matricularse.")

        # Selección de curso
        curso = input("Ingrese el curso (Inglés 0 / Inglés 1 / Inglés 2 / Inglés 3 / Inglés 4 / Inglés 5): ").strip()
        sede = input("Ingrese la sede (Virtual): ").strip()
        horario = input("Ingrese el horario (mañana / tarde / noche): ").strip().lower()

        # Generar código de pago simple
        codigo_pago = f"PAGO{nombre[:3].upper()}{randint(100,999)}"

        # Mostrar factura simulada
        print("\n--- FACTURA ---")
        print("Alumno:", nombre)
        print("Curso:", curso)
        print("Sede:", sede)
        print("Horario:", horario)
        print("Código de pago:", codigo_pago)
        print("--------------------")

        # Guardar en memoria (opcional)
        alumnos_matriculados.append({
            "nombre": nombre,
            "curso": curso,
            "sede": sede,
            "horario": horario,
            "codigo_pago": codigo_pago
        })

        # Guardar en la base de datos
        cursor.execute("""
        INSERT INTO alumnos (nombre, curso, sede, horario, codigo_pago)
        VALUES (?, ?, ?, ?, ?)
        """, (nombre, curso, sede, horario, codigo_pago))
        conn.commit()

    else:
        print("El alumno no puede matricularse por tener deudas pendientes o estar inactivo.")

    # Preguntar si desea registrar otro alumno
    continuar = input("¿Desea registrar otro alumno? (sí/no): ").strip().lower()
    if continuar != "sí":
        break

# Mostrar lista final desde la base de datos
print("\nLista de alumnos matriculados:")
cursor.execute("SELECT nombre, curso, sede, horario, codigo_pago FROM alumnos")
for row in cursor.fetchall():
    print(f"- {row[0]} ({row[1]}, {row[2]}, {row[3]}, Código: {row[4]})")

# Cerrar conexión
conn.close()
