import mysql.connector
from faker import Faker

# Initialize faker
fake = Faker()

# Generate random dummy data for customers
def generate_customer_data(num_customers):
    customer_data = []
    for customer_id in range(1, num_customers + 1):
        first_name = fake.first_name()
        last_name = fake.last_name()
        address = fake.address()[:50]
        phone_no = fake.phone_number()[:15]
        email_address = fake.email()[:30]
        customer_data.append((f"CUS{customer_id:03}", first_name, last_name, address, phone_no, email_address))
    return customer_data

# Insert data into MySQL database
def insert_customer_data_into_mysql(customer_data):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mycart"
    )
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer (
            customer_id VARCHAR(10) PRIMARY KEY,
            first_name VARCHAR(20),
            last_name VARCHAR(20),
            address VARCHAR(50),
            phone_no VARCHAR(15),
            email_address VARCHAR(30)
        )
    ''')

    # Insert customer data into the table
    insert_query = "INSERT INTO customer (customer_id, first_name, last_name, address, phone_no, email_address) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.executemany(insert_query, customer_data)

    conn.commit()
    conn.close()

# Number of customers to generate
num_customers = 50

customer_data = generate_customer_data(num_customers)
insert_customer_data_into_mysql(customer_data)
