import mysql.connector



def setup():
    con = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="secret",
        database="soldiers_db"
    )

    crs = con.cursor()
    crs.execute("use soldiers_db;")
    crs.execute("""
    CREATE TABLE IF NOT EXISTS soldiers (
        id int primary key auto_increment,
        name VARCHAR(100) NOT NULL,
        soldier_rank VARCHAR(50),
        unit VARCHAR(100),
        active BOOLEAN DEFAULT TRUE
    )
    """)

    print("table soldiers created!")

    crs.execute("describe soldiers;")
    # data = crs.fetchall()

    con.commit()
    crs.close()
    con.close()

    # print(data)
