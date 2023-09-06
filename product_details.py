import random
import mysql.connector
from faker import Faker

# Initialize faker
fake = Faker()

# Generate random dummy data for product details
def generate_product_details_data(num_products, num_vendors):
    product_details = []
    for product_id in range(1, num_products + 1):
        vendor_id = random.randint(1, num_vendors)  # Choose a random vendor_id
        price = random.randint(100, 1000)
        quantity = random.randint(1, 50)
        size = random.choice(['l', 'xl', 'xxl', 'xxxl'])
        colour = fake.color_name()[:10]
        
        # Format product_id as ABC001
        product_id_formatted = f"ABC{product_id:03}"
        
        product_details.append((product_id_formatted, vendor_id, price, quantity, size, colour))
    return product_details

# Insert data into MySQL database
def insert_product_details_into_mysql(product_details):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mycart"
    )
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS product_details (
            product_id VARCHAR(10) PRIMARY KEY,
            vendor_id INT,
            price INT(4),
            quantity INT(50),
            size VARCHAR(10),
            colour VARCHAR(10),
            FOREIGN KEY (vendor_id) REFERENCES vendor_details(vendor_id)
        )
    ''')

    # Insert product details data into the table
    insert_query = "INSERT INTO product_details (product_id, vendor_id, price, quantity, size, colour) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.executemany(insert_query, product_details)

    conn.commit()
    conn.close()

# Number of products and vendors to generate
num_products = 100
num_vendors = 50
product_details_data = generate_product_details_data(num_products, num_vendors)

insert_product_details_into_mysql(product_details_data)
