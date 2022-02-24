import psycopg2

connection = psycopg2.connect(
    database="new_marina_db",
    host="localhost",
    port="5432",
    user="postgres",
    password="postgres"
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM users;")

users = cursor.fetchall()

for user in users:
    print(users)