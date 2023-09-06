import mysql.connector

# Replace these with your actual database credentials
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "mycart"
}


# Connect to the database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Disable foreign key checks
cursor.execute("SET FOREIGN_KEY_CHECKS = 0")

# Get a list of all tables in the database
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

# Loop through the tables and drop them
for table in tables:
    table_name = table[0]
    drop_table_query = f"DROP TABLE IF EXISTS {table_name}"
    cursor.execute(drop_table_query)
    print(f"Dropped table: {table_name}")

# Enable foreign key checks back
cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

# Commit the changes and close the connection
connection.commit()
connection.close()
