import mysql.connector
import time

# המתנה קצרה כדי לוודא ש-MySQL מוכן (במיוחד עם Docker)
time.sleep(2)

# חיבור ל-MySQL
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="secret",
    database="tests"
)
conn.cursor()
# יצירת cursor לעבודה עם SQL
cursor = conn.cursor()

# SQL ליצירת טבלה
create_table_sql = """
CREATE TABLE IF NOT EXISTS tests4 (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    soldier_rank VARCHAR(50),
    unit VARCHAR(100),
    active BOOLEAN DEFAULT TRUE
)
"""

# הרצת ה-SQL
cursor.execute(create_table_sql)

# שמירת השינויים
conn.commit()

print("Table created successfully.")

# סגירת משאבים
cursor.close()
conn.close()