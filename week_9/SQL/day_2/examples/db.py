import mysql.connector

def get_connector():
    return mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="secret",
        database="soldiers_db"
    )

def create(name: str, soldier_rank: str, unit: str):
    connector = get_connector()
    cursor = connector.cursor()
    add_soldier_text = """
    insert into soldiers (name, soldier_rank, unit) 
    values (%s, %s, %s)
    """
    val = name, soldier_rank, unit
    cursor.execute(add_soldier_text, val)
    connector.commit()
    cursor.close()
    connector.close()

    last_id = cursor.lastrowid
    return last_id


def update(soldier_id: int, data: dict):
    connector = get_connector()
    cursor = connector.cursor()

    parts = [f"{key} = %s" for key in data.keys()]
    claus = " ,".join(parts)

    text = f"""
    update soldiers
    set {claus}
    WHERE id = %s;
    """
    values = list(data.values()) + [soldier_id]

    cursor.execute(text, values)
    connector.commit()

    cursor.close()
    connector.close()

    changed = cursor.rowcount
    return changed


def delete(soldier_id: int):
    connector = get_connector()
    cursor = connector.cursor()
    sql_txt = """
    delete from soldiers
    where id = %s
    """
    cursor.execute(sql_txt, [soldier_id])

    connector.commit()
    deleted = cursor.rowcount > 0

    return deleted


def get_all_soldiers():
    connector = mysql.connector.connect(host="localhost",port=3306,database="soldiers_db",user="root",password="secret")
    cursor = connector.cursor()

    sql_txt = """SELECT * FROM soldiers;
    """

    cursor.execute(sql_txt)

    data = cursor.fetchall()
    # connector.commit()

    cursor.close()
    connector.close()

    return data


def get_by_id(soldier_id: int):
    connector = mysql.connector.connect(host="127.0.0.1", port=3306, user="root", password="secret", database="soldiers_db")
    cursor = connector.cursor(dictionary=True)
    sql_txt = """SELECT * FROM soldiers where id = %s;
    """

    cursor.execute(sql_txt, [soldier_id])

    data = cursor.fetchone()
    if data:
        return data
    return None


if __name__ == "__main__":
    # last_id = create("Zvulun Ben Yaakov", "Banshak", "unit ejept")
    # print(last_id)

    # sol_dict = {"name": "Bin",
    # "soldier_rank": "gu",
    # "unit": 1}

    # is_change = update(18 ,sol_dict)
    # print(is_change)

    # is_deleted = delete(18)
    # print(is_deleted)

    # print(get_all_soldiers())

    # print(get_by_id(18))


    pass

