import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute(
    'SELECT name, weight FROM clients WHERE weight > 50',
    {'weight' : 50}
    )
connection.commit()

cursor.execute('CREATE TABLE IF NOT EXISTS clients ('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
')')

cursor.execute(
    'INSERT INTO clients (name, weight) VALUES (?, ?)', 
    ('Gabriel', 60.5)
    )
cursor.execute(
    'INSERT INTO clients (name, weight) VALUES (:name, :weight)', 
    {'name' : 'Maria', 'weight' : 82.4}
    )
cursor.execute(
    'INSERT INTO clients VALUES (:id, :name, :weight)', 
    {'id' : None, 'name' : 'Daniel', 'weight' : 110.7}
    )
connection.commit()

cursor.execute('SELECT * FROM clients')

for line in cursor.fetchall():
    identifier, name, weight = line
    print(identifier, name, weight)

cursor.close()
connection.close()