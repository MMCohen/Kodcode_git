import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="secret",
        database="soldiers_db",
        )

def get_schema() -> list:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DESCRIBE soldiers")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    # each row is (Field, Type, Null, Key, Default, Extra)
    # return rows
    return [{"column": row[0], "type": row[1]} for row in rows]


def create(name: str, rank: str, unit: str) -> int:
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
        INSERT INTO soldiers (name, soldier_rank, unit)
        VALUES (%s, %s, %s)
    """
    values = (name, rank, unit)

    cursor.execute(sql, values)
    conn.commit()

    # MySQL gives us the id it assigned
    new_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return new_id

def update():
    pass


if __name__ == "__main__":

    # new_id = create("moshe", "master privet", "8200")
    # print(new_id)
    print(get_schema())
    pass