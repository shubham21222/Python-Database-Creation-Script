import random
import mysql.connector
from faker import Faker

# Initialize faker
fake = Faker()

# Generate random dummy data for orders
def generate_order_data(num_orders, product_ids, discount_ids, customer_ids, category_ids):
    order_data = []
    for order_id in range(2100, 2100 + num_orders):
        product_id = random.choice(product_ids)
        discount_id = random.choice(discount_ids)
        customer_id = random.choice(customer_ids)
        order_status = random.choice(['pending', 'success'])
        category_id = random.choice(category_ids)
        amount = random.randint(50, 500)
        order_data.append((order_id, product_id, discount_id, customer_id, order_status, category_id, amount))
    return order_data

# Insert data into MySQL database
def insert_order_data_into_mysql(order_data):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mycart"
    )
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id INT PRIMARY KEY,
            product_id VARCHAR(10),
            discount_id VARCHAR(10),
            customer_id VARCHAR(10),
            order_status VARCHAR(10),
            category_id VARCHAR(10),
            amount INT,
            FOREIGN KEY (product_id) REFERENCES product_details(product_id),
            FOREIGN KEY (discount_id) REFERENCES discounts(discount_id),
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
            FOREIGN KEY (category_id) REFERENCES categories(category_id)
        )
    ''')

    # Insert order data into the table
    insert_query = "INSERT INTO orders (order_id, product_id, discount_id, customer_id, order_status, category_id, amount) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(insert_query, order_data)

    conn.commit()
    conn.close()

# Number of orders to generate
num_orders = 50

# Lists of available IDs for foreign keys (replace with your actual data)
product_ids = ["ABC001", "ABC002", "ABC003"]
discount_ids = ["DES20", "DES30", "DES40"]
customer_ids = ["CUS212", "CUS213", "CUS214"]
category_ids = ["CAT001", "CAT002", "CAT003"]

order_data = generate_order_data(num_orders, product_ids, discount_ids, customer_ids, category_ids)
insert_order_data_into_mysql(order_data)
