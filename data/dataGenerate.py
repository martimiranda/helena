import sqlite3
import random
from faker import Faker
from datetime import datetime

# Crear una instancia de Faker para generar datos falsos
fake = Faker()

# Conectar a la base de datos
conn = sqlite3.connect('data/data.db')
cursor = conn.cursor()

# Función para insertar datos en la tabla Client
def insert_client():
    nom = fake.first_name()
    cognoms = fake.last_name()
    telefon = fake.phone_number()
    client_antic = random.choice([0, 1, None])  # Cliente antiguo puede ser 0, 1 o NULL
    color = fake.color_name()

    cursor.execute('''
        INSERT INTO Client (Nom, Cognoms, Telefon, Client_antic, Color)
        VALUES (?, ?, ?, ?, ?)
    ''', (nom, cognoms, telefon, client_antic, color))

    conn.commit()
    return cursor.lastrowid  # Devuelve el ID del cliente insertado

# Función para insertar datos en la tabla Serveis
def insert_servei(client_id):
    fecha = fake.date_this_decade()  # Fecha en esta década
    preu = round(random.uniform(10.0, 100.0), 2)  # Precio aleatorio entre 10 y 100
    servei = fake.word()  # Servicio como una palabra aleatoria

    cursor.execute('''
        INSERT INTO Serveis (Client_id, Fecha, Preu, Servei)
        VALUES (?, ?, ?, ?)
    ''', (client_id, fecha, preu, servei))

    conn.commit()

# Insertar varios clientes y servicios asociados
for _ in range(10):  # Inserta 10 clientes
    client_id = insert_client()
    for _ in range(random.randint(1, 5)):  # Cada cliente puede tener entre 1 y 5 servicios
        insert_servei(client_id)

# Cerrar la conexión
conn.close()

print("Datos generados exitosamente.")
