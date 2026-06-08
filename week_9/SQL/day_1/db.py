import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="secret",
        database="soldiers_db"
    )
    pass

def get_schema():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("describe soldiers;")
    data = cursor.fetchall()
    return [{"field" :row[0], "type" :row[1]} for row in data]

add_column ="""
alter table soldiers
add created_at DATETIME DEFAULT NOW()
"""

add_soldier = """
insert into soldiers (name, soldier_rank, unit, active)
values ("david", "priv", 8200, 1)
"""

con = get_connection()
cursor = con.cursor()
cursor.execute(add_soldier)
con.commit()
cursor.close()
con.close()