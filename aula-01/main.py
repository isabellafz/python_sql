import sqlite3
from pathlib import Path  

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()


#Cuidado: fazendo delete sem where
# cursor.execute(
#     f'DELETE FROM {TABLE_NAME}'
# )

connection.commit()

# DELETE COM WHERE
# cursor.execute(
#     f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
# )

# connection.commit()

# SQL
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Registrar valores na tabela
sql = (
    f'INSERT INTO {TABLE_NAME} (name, weight) '
    'VALUES (:name, :weight)'
)

cursor.execute(sql, {'name': 'Robson', 'weight': 100})
cursor.executemany(
    sql, 
    (
        {'name': 'Arrascaeta', 'weight': 64},
        {'name': 'Gabigol', 'weight': 83},
        {'name': 'Pedro', 'weight': 85},
        {'name': 'Cunha', 'weight': 80},
    )
)

# cursor.execute(sql, ['Joana', 4])
# cursor.executemany(
#     sql,
#     (
#         ('Pedrosa', 67), ('Murillao', 96)
#     )
# )

connection.commit()





if __name__ == '__main__':
    print(sql)
    
    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "3"'
    )
    
    connection.commit()
        
    cursor.execute(
        f'UPDATE {TABLE_NAME} '
        'SET name="VALOR NOVO", weight="230" '
        'WHERE id = "2"'
    )
    
    connection.commit()
    cursor.execute(
        f'SELECT * FROM {TABLE_NAME} '
        'WHERE id = "3"'
    )
    
    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight )
    
    
    cursor.close()
    connection.close()
# CRUD = Create, Read, Update, Delete
# SQL =  INSERT, SELECT, UPDATE, DELETE