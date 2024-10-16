import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conn = sqlite3.connect('data/data.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear la tabla Client
cursor.execute('''
CREATE TABLE IF NOT EXISTS Client (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,  -- ID autogenerado
    Nom TEXT NOT NULL,                     -- Nombre obligatorio
    Cognoms TEXT,                          -- Apellidos opcional
    Telefon TEXT,                          -- Teléfono opcional
    Client_antic INTEGER,                  -- Cliente antiguo (1 = sí, 0 = no, NULL = no definido)
    Color TEXT                             -- Color opcional
);
''')

# Crear la tabla Serveis
cursor.execute('''
CREATE TABLE IF NOT EXISTS Serveis (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,  -- ID autogenerado para el servicio
    Client_id INTEGER,                     -- Relación con la tabla Client
    Fecha DATE,                            -- Fecha del servicio
    Preu REAL,                             -- Precio del servicio
    Servei TEXT,                           -- Descripción del servicio
    FOREIGN KEY (Client_id) REFERENCES Client(Id) -- Relación con el cliente
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Serveis_oferits (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,  -- ID autogenerado para el servicio
    Preu REAL,                             -- Precio del servicio
    Servei TEXT
);
''')



# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Las tablas 'Client' y 'Serveis' han sido creadas en la base de datos.")
