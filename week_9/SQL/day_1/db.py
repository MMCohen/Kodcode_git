import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="secret",
        database="soldiers_db"
    )

def get_schema():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("describe soldiers;")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"field" :row[0], "type" :row[1]} for row in data]