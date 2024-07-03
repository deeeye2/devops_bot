import sqlite3

conn = sqlite3.connect('/app/database.db')
cursor = conn.cursor()

# Print the names of the tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)

# Print the schema of each table
for table_name in tables:
    table_name = table_name[0]
    cursor.execute(f"PRAGMA table_info({table_name});")
    schema = cursor.fetchall()
    print(f"Schema of {table_name}:")
    for column in schema:
        print(column)

conn.close()
