import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Conexión a MySQL exitosa")
    except Error as e:
        print(f"Error '{e}' al conectar a MySQL")

    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query ejecutada exitosamente")
    except Error as e:
        print(f"Error '{e}' al ejecutar query")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Error '{e}' al leer datos")

# Conectar a la base de datos
connection = create_connection("localhost", "root", "password", "database_name")

# Crear una tabla
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT, 
  name TEXT NOT NULL, 
  age INT, 
  gender TEXT, 
  nationality TEXT, 
  PRIMARY KEY (id)
) ENGINE = InnoDB
"""
execute_query(connection, create_table_query)

# Insertar datos en la tabla
insert_user_query = """
INSERT INTO
  `users` (`name`, `age`, `gender`, `nationality`)
VALUES
  ('James', 25, 'male', 'USA');
"""
execute_query(connection, insert_user_query)

# Leer datos de la tabla
select_users_query = "SELECT * FROM users"
users = execute_read_query(connection, select_users_query)

for user in users:
    print(user)
