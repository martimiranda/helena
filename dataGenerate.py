import sqlite3
import random

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('data.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Generar datos ficticios para 100 clientes
nombres = ['Helena', 'Carla', 'Marta', 'Joan', 'Alex', 'Marc', 'Sofia', 'Laura', 'Maria', 'Cristina']
apellidos = ['Garcia', 'Martinez', 'Lopez', 'Sanchez', 'Gomez', 'Fernandez', 'Ruiz', 'Diaz', 'Perez', 'Torres']
colores = ['rojo', 'azul', 'verde', 'negro', 'blanco', 'morado', 'amarillo']

# Insertar 100 registros en la tabla Client
for i in range(100):
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    telefono = f'6{random.randint(10000000, 99999999)}'  # Genera un teléfono aleatorio que empieza por 6
    client_antic = random.choice([0, 1, None])  # Cliente antiguo puede ser 0, 1 o NULL
    color = random.choice(colores)
    
    cursor.execute('''
        INSERT INTO Client (Nom, Cognoms, Telefon, Client_antic, Color)
        VALUES (?, ?, ?, ?, ?)
    ''', (nombre, apellido, telefono, client_antic, color))

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("100 registros de clientes han sido insertados en la tabla 'Client'.")
