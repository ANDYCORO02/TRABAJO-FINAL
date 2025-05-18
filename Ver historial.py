import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect("matriculas.db")
cursor = conn.cursor()

# Obtener todos los registros
cursor.execute("SELECT nombre, curso, sede, horario, codigo_pago FROM alumnos")
alumnos = cursor.fetchall()

# Mostrar los datos
print("\n--- LISTA DE ALUMNOS MATRICULADOS ---")
for alumno in alumnos:
    print(f"- {alumno[0]} ({alumno[1]}, {alumno[2]}, {alumno[3]}, Código: {alumno[4]})")

# Cerrar conexión
conn.close()

