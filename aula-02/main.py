#PyMySQL - um clássico MySQL feito em python puro
import os
import  pymysql
import dotenv

TABLE_NAME = 'users'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4'
)
cursor = connection.cursor()

#SQL
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS  {TABLE_NAME} ('
    'id INT NOT NULL AUTO_INCREMENT, '
    'nome VARCHAR(50) NOT NULL, '
    'idade INT NOT NULL, '
    'PRIMARY KEY (id) '
    ') '

)

connection.commit()
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(nome, idade) VALUES (%s, %s) '
)
cursor.execute(sql, ('Isabella', 17))

connection.commit()

sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(nome, idade) VALUES (%(nome)s, %(idade)s) '
)


# trabalhando com valores de dicionario
data = {
    "nome": 'Pedrosa',
    "idade": 19
}
cursor.execute(sql, data)

connection.commit()

sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(nome, idade) '
    'VALUES (%(name)s, %(age)s ) '
)

data3 = (
    {"name": "Murillo", "age": 19},
    {"name": "Isabella", "age": 17},
    {"name": "Pedrosa", "age": 19},
    {"name": "Italo", "age": 5},
    {"name": "Gabriel", "age": 11},
)

cursor.executemany(sql, data3)
connection.commit()

sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(nome, idade) '
    'VALUES (%s, %s ) '
)

data4 = (
    ("Ruth", 85),
    ("Maria", 81),
    ("Alencar", 76),
    ("Fátima", 67),
    ("Antônio", 70),
)

cursor.executemany(sql, data4)
connection.commit()

sql2 = (
    f'INSERT INTO {TABLE_NAME} '
    '(nome, idade) VALUES (%s, %s) '
)

nome = input('Digite seu nome:  ')
idade = input('Digite sua idade:  ')
cursor.execute(sql2, (nome, idade))

connection.commit()

# Usando o SELECT

sql = (
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id = 5'
    
)
cursor.execute(sql)

data5= cursor.fetchall()

for row in data5:
    print(row)

menor_id = int(input('Digite o menor id: '))
maior_id = int(input('Digite o maior id: '))
sql = (
    f'SELECT * FROM {TABLE_NAME} '
    'WHERE id BETWEEN %s AND %s'
    
)
cursor.execute(sql, (menor_id, maior_id))
print(cursor.mogrify(sql, (menor_id, maior_id)))

data6= cursor.fetchall()

for row2 in data6:
    print(row2)
    
    
    
# utilizando o Delete

sql = (
    f'DELETE FROM {TABLE_NAME} '
    'WHERE id = %s'
)
cursor.execute(sql, (8))
connection.commit()


# Usando Update

sql = (
    f'UPDATE {TABLE_NAME} '
    'SET nome=%s, idade=%s '
    'WHERE id = %s '
)

cursor.execute(sql, ('Usei o Update poha', 900, 1))
connection.commit()

cursor.close()
connection.close()