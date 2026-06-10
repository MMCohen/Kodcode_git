import mysql.connector

def get_connector():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="secret",
        database="soldiers_db",
    )


def get_summary():
    """
    :return: dict with total soldiers, active soldiers and inactive soldiers
    """
    data_dict = dict()

    connector = get_connector()
    cursor = connector.cursor(dictionary=True)

    cursor.execute("select count(*) as total from soldiers;")
    data_dict.update(cursor.fetchone())

    cursor.execute("select count(*) as active from soldiers where active = 1;")
    data_dict.update(cursor.fetchone())

    cursor.execute("select count(*) as inactive from soldiers where active = 0;")
    data_dict.update(cursor.fetchone())

    cursor.close()
    connector.close()

    return data_dict


def count_by_unit():
    """
    :return: list of dicts with [{"unit": "8200", "total": 4}, ...]
    """
    connector = get_connector()
    cursor = connector.cursor(dictionary=True)

    cursor.execute("""
    SELECT unit, count(unit) as total
    FROM soldiers
    GROUP BY unit;
    """)
    data = cursor.fetchall()
    cursor.close()
    connector.close()

    return data

if __name__ == "__main__":
    # print(get_summary())
    print(count_by_unit())
    # print(get_summary())
