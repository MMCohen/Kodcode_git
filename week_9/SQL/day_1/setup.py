import mysql.connector

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
    grade_max int,
    total_grade int,
    t_note varchar(250)
)
""")

print("table soldiers created!")

crs.execute("describe soldiers;")
x= crs.fetchall()
print(x)

crs.close()
con.close()
