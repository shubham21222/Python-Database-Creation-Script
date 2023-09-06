import random
import mysql.connector
from faker import Faker

# Initialize faker
fake = Faker()

# Generate random dummy data for vendor details
def generate_vendor_details_data(num_vendors):
    vendor_details = []
    for vendor_id in range(1, num_vendors + 1):
        account_id = vendor_id  # Use vendor_id as account_id
        bank_account_number = random.randint(100000000000000, 999999999999999)
        ifsc_code = fake.random_element(elements=("ABCD1234567", "EFGH8901234", "IJKL5678901"))
        gst_number = fake.random_element(elements=("GST123456789", "GST987654321"))
        vendor_details.append((account_id, vendor_id, bank_account_number, ifsc_code, gst_number))
    return vendor_details

# Insert data into MySQL database
def insert_vendor_details_into_mysql(vendor_details):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mycart"
    )
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendor_details (
            account_id INT PRIMARY KEY,
            vendor_id INT,
            bank_account_number BIGINT(15),
            ifsc_code VARCHAR(15),
            gst_number VARCHAR(15),
            FOREIGN KEY (vendor_id) REFERENCES Registration(vendor_id)
        )
    ''')

    # Insert vendor details data into the table
    insert_query = "INSERT INTO vendor_details (account_id, vendor_id, bank_account_number, ifsc_code, gst_number) VALUES (%s, %s, %s, %s, %s)"
    cursor.executemany(insert_query, vendor_details)

    conn.commit()
    conn.close()

# Number of vendors to generate
num_vendors = 50
vendor_details_data = generate_vendor_details_data(num_vendors)

insert_vendor_details_into_mysql(vendor_details_data)
