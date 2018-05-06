#Cria um banco de dados que armazene o nome das faces correspondentes.
#Estou utilizando o SQLite 3 para este propósito.

import sqlite3

conn = sqlite3.connect('database.db')

c = conn.cursor()

sql = """
DROP TABLE IF EXISTS usuarios;
CREATE TABLE usuarios (
           id integer unique primary key autoincrement,
           nome text
);
"""

c.executescript(sql)

conn.commit()

conn.close()