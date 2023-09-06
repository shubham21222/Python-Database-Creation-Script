import random
import mysql.connector
from faker import Faker

# Initialize faker
fake = Faker()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mycart"
)
cursor = conn.cursor()

# Generate random dummy data for vendors
def generate_vendor_data(num_vendors):
    registration = []
    for vendor_id in range(1, num_vendors + 1):
        first_name = fake.first_name()
        last_name = fake.last_name()
        address = fake.address()
        email = fake.email()
        registration.append((vendor_id, first_name, last_name, address, email))
    return registration

# Insert data into MySQL database
def insert_registration_into_mysql(registration):
    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registration(
            vendor_id INT PRIMARY KEY,
            first_name VARCHAR(25),
            last_name VARCHAR(25),
            address VARCHAR(100),
            email VARCHAR(255)
        )
    ''')

    # Insert vendor data into the table
    insert_query = "INSERT INTO registration (vendor_id, first_name, last_name, address, email) VALUES (%s, %s, %s, %s, %s)"
    cursor.executemany(insert_query, registration)

    conn.commit()

# Number of registration to generate
num_registration = 50
vendor_data = generate_vendor_data(num_registration)
insert_registration_into_mysql(vendor_data)

# Close the cursor and connection
cursor.close()
conn.close()
