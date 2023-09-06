import mysql.connector
from faker import Faker
import random

# Initialize faker
fake = Faker()

# Create a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mycart"
)
cursor = conn.cursor()

# Generate random dummy data for the category table
def generate_category_data(num_categories, product_ids):
    category_data = []
    product_id_iter = iter(product_ids)
    
    for category_id in range(1, num_categories + 1):
        product_id = next(product_id_iter)
        product_name = fake.word() + " " + fake.word()  # Combine two random words for product name
        brand_name = fake.company()
        gender = random.choice(["Male", "Female", "Unisex"])
        category_data.append((category_id, product_id, product_name, brand_name, gender))
    return category_data

# Insert data into MySQL database
def insert_category_data_into_mysql(category_data):
    # Create the category table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS category (
            category_id INT PRIMARY KEY,
            product_id VARCHAR(10),
            product_name VARCHAR(100),
            brand_name VARCHAR(50),
            gender VARCHAR(10),
            FOREIGN KEY (product_id) REFERENCES product_details(product_id)
        )
    ''')

    # Insert category data into the table
    insert_query = "INSERT INTO category (category_id, product_id, product_name, brand_name, gender) VALUES (%s, %s, %s, %s, %s)"
    cursor.executemany(insert_query, category_data)

    conn.commit()

# Number of categories to generate
num_categories = 100

# Generate product IDs in the format "ABC001" to "ABC100"
product_ids = [f"ABC{str(i).zfill(3)}" for i in range(1, num_categories + 1)]

category_data = generate_category_data(num_categories, product_ids)
insert_category_data_into_mysql(category_data)

# Close the connection
conn.close()
