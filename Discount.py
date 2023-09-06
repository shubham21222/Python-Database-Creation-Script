import random
import mysql.connector

# Generate random dummy data for discounts
def generate_discount_data(num_discounts, product_ids):
    discount_data = []
    for discount_id in range(1, num_discounts + 1):
        product_id = random.choice(product_ids)
        max_discount = 15  # Max total discount of 15%
        seasonal_discount = random.randint(0, min(5, max_discount))  # Up to 5% discount or max_discount, whichever is smaller
        max_promotional_discount = max_discount - seasonal_discount
        promotional_discount = random.randint(0, max_promotional_discount)  # Up to remaining discount
        discount_data.append((f"DES{discount_id:02}", product_id, seasonal_discount, promotional_discount))
    return discount_data

# Insert data into MySQL database
def insert_discount_data_into_mysql(discount_data):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mycart"
    )
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS discounts (
            discount_id VARCHAR(10) PRIMARY KEY,
            product_id VARCHAR(10),
            seasonal_discount INT,
            promotional_discount INT,
            CONSTRAINT chk_seasonal_discount CHECK (seasonal_discount <= 5),
            CONSTRAINT chk_promotional_discount CHECK (promotional_discount <= 15),
            CONSTRAINT chk_total_discount CHECK (seasonal_discount + promotional_discount <= 15),
            FOREIGN KEY (product_id) REFERENCES product_details(product_id)
        )
    ''')

    # Insert discount data into the table
    insert_query = "INSERT INTO discounts (discount_id, product_id, seasonal_discount, promotional_discount) VALUES (%s, %s, %s, %s)"
    cursor.executemany(insert_query, discount_data)

    conn.commit()
    conn.close()

# Number of discounts to generate
num_discounts = 20

# List of available product IDs (replace with your actual data)
product_ids = ["ABC001", "ABC002", "ABC003"]

discount_data = generate_discount_data(num_discounts, product_ids)
insert_discount_data_into_mysql(discount_data)
