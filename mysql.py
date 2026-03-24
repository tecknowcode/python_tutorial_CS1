import mysql.connector

# connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="toor",
    database="college"
)

cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS student(
    id INT PRIMARY KEY,
    name VARCHAR(50),
    marks INT
)
""")

# insert data
cursor.execute("INSERT INTO student VALUES (1, 'Amit', 80)")
cursor.execute("INSERT INTO student VALUES (2, 'Neha', 90)")
cursor.execute("INSERT INTO student VALUES (3, 'Ravi', 75)")

conn.commit()

# fetch data
cursor.execute("SELECT * FROM student")

rows = cursor.fetchall()

print("Student Records:")
for row in rows:
    print(row)

# close connection
conn.close()