import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('data/data.db')
cursor = conn.cursor()

# Función para limpiar las tablas
def limpiar_tablas():
    # Eliminar todas las filas de la tabla Serveis
    cursor.execute('DELETE FROM Serveis')
    
    # Eliminar todas las filas de la tabla Client
    cursor.execute('DELETE FROM Client')
    
    # Confirmar los cambios
    conn.commit()

# Ejecutar la limpieza de las tablas
limpiar_tablas()

# Cerrar la conexión
conn.close()

print("Base de datos limpiada exitosamente.")
