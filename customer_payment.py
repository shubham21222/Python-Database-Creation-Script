import random
import mysql.connector
from itertools import cycle

# Generate random dummy data for customer payments
def generate_customer_payment_data(num_customer_payments, customer_ids, payment_method_codes):
    customer_payment_data = []
    customer_id_cycle = cycle(customer_ids)
    
    for payment_id in range(1, num_customer_payments + 1):
        customer_id = next(customer_id_cycle)
        payment_method_code = random.choice(payment_method_codes)
        customer_payment_data.append((f"CPA{payment_id:04}", customer_id, payment_method_code))
        
    return customer_payment_data

# Insert data into MySQL database
def insert_customer_payment_data_into_mysql(customer_payment_data):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mycart"
    )
    cursor = conn.cursor()

    # Insert customer payment data into the table
    insert_query = "INSERT INTO customer_payment (customer_payment_id, customer_id, payment_method_code) VALUES (%s, %s, %s)"
    cursor.executemany(insert_query, customer_payment_data)

    conn.commit()
    conn.close()

# Number of customer payments to generate
num_customer_payments = 50

# Generate a list of customer IDs from CUS001 to CUS050
customer_ids = [f"CUS{num:03}" for num in range(1, num_customer_payments + 1)]

# List of available payment method codes (replace with your actual data)
payment_method_codes = ["PY00001", "PY00002", "PY00003", "PY00004", "PY00005"]

customer_payment_data = generate_customer_payment_data(num_customer_payments, customer_ids, payment_method_codes)
insert_customer_payment_data_into_mysql(customer_payment_data)
