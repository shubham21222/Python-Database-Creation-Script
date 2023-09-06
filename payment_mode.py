import mysql.connector

# Insert data into MySQL database
def insert_payment_method_data_into_mysql(payment_method_data):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mycart"
    )
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payment_method (
            payment_method_id VARCHAR(10) PRIMARY KEY,
            payment_method_name VARCHAR(50)
        )
    ''')

    # Insert payment method data into the table
    insert_query = "INSERT INTO payment_method (payment_method_id, payment_method_name) VALUES (%s, %s)"
    cursor.executemany(insert_query, payment_method_data)

    conn.commit()
    conn.close()

# Payment method data
payment_method_data = [
    ("PY00001", "Credit Card"),
    ("PY00002", "Debit Card"),
    ("PY00003", "PayPal"),
    ("PY00004", "Cash on Delivery"),
    ("PY00005", "Bank Transfer")
]

insert_payment_method_data_into_mysql(payment_method_data)
