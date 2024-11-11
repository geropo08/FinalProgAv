import sqlite3

def conectar_db():
    conn = sqlite3.connect('BD.db')
    return conn

def crear_tablas(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        edad INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        ciudad TEXT NOT NULL,
        edad INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        producto TEXT NOT NULL,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ventas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        producto TEXT NOT NULL,
        cantidad INTEGER NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS empleados (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        puesto TEXT NOT NULL,
        salario INTEGER NOT NULL
    )
    ''')
def insertar_datos(cursor):
    cursor.execute('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', ('Alice', 30))
    cursor.execute('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', ('Bob', 15))
    cursor.execute('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', ('Carlos', 20))
    cursor.execute('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', ('Diana', 25))
    cursor.execute('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', ('Elias', 45))

    cursor.execute('INSERT INTO clientes (nombre, ciudad, edad) VALUES (?, ?, ?)', ('Cliente1', 'Madrid', '17'))
    cursor.execute('INSERT INTO clientes (nombre, ciudad, edad) VALUES (?, ?, ?)', ('Cliente2', 'Barcelona', '40'))
    cursor.execute('INSERT INTO clientes (nombre, ciudad, edad) VALUES (?, ?, ?)', ('Cliente3', 'Madrid', '31'))
    cursor.execute('INSERT INTO clientes (nombre, ciudad, edad) VALUES (?, ?, ?)', ('Cliente4', 'Valencia', '10'))
    cursor.execute('INSERT INTO clientes (nombre, ciudad, edad) VALUES (?, ?, ?)', ('Cliente5', 'Sevilla', '19'))

    cursor.execute('INSERT INTO pedidos (cliente_id, producto) VALUES (?, ?)', (1, 'ProductoA'))
    cursor.execute('INSERT INTO pedidos (cliente_id, producto) VALUES (?, ?)', (2, 'ProductoB'))
    cursor.execute('INSERT INTO pedidos (cliente_id, producto) VALUES (?, ?)', (3, 'ProductoC'))
    cursor.execute('INSERT INTO pedidos (cliente_id, producto) VALUES (?, ?)', (4, 'ProductoD'))
    cursor.execute('INSERT INTO pedidos (cliente_id, producto) VALUES (?, ?)', (5, 'ProductoE'))

    cursor.execute('INSERT INTO ventas (producto, cantidad) VALUES (?, ?)', ('ProductoA', 10))
    cursor.execute('INSERT INTO ventas (producto, cantidad) VALUES (?, ?)', ('ProductoB', 5))
    cursor.execute('INSERT INTO ventas (producto, cantidad) VALUES (?, ?)', ('ProductoC', 20))
    cursor.execute('INSERT INTO ventas (producto, cantidad) VALUES (?, ?)', ('ProductoD', 15))
    cursor.execute('INSERT INTO ventas (producto, cantidad) VALUES (?, ?)', ('ProductoE', 25))

    cursor.execute('INSERT INTO empleados (nombre, puesto, salario) VALUES (?, ?, ?)', ('Juan', 'ingeniero', 3000))
    cursor.execute('INSERT INTO empleados (nombre, puesto, salario) VALUES (?, ?, ?)', ('Maria', 'administrativa', 2500))
    cursor.execute('INSERT INTO empleados (nombre, puesto, salario) VALUES (?, ?, ?)', ('Luis', 'supervisor', 3500))
    cursor.execute('INSERT INTO empleados (nombre, puesto, salario) VALUES (?, ?, ?)', ('Ana', 'contadora', 2800))
    cursor.execute('INSERT INTO empleados (nombre, puesto, salario) VALUES (?, ?, ?)', ('Pedro', 'marketing', 2700))

def ejecutar_consulta(cursor, sql, params=()):
    cursor.execute(sql, params)
    return cursor.fetchall()

def main():
    conn = conectar_db()
    cursor = conn.cursor()

    crear_tablas(cursor)
    insertar_datos(cursor)

    conn.commit()  
    while True:
        consulta = input("Introduce tu consulta SQL (o 'salir' para terminar): ")
        if consulta.lower() == 'salir':
            break
        try:
            resultados = ejecutar_consulta(cursor, consulta)
            for fila in resultados:
                print(fila)
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")

    conn.close()

if __name__ == "__main__":
    main()