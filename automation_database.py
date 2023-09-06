import mysql.connector
import time
from sql_database import generate_vendor_data, insert_registration_into_mysql
from account_details import generate_vendor_details_data, insert_vendor_details_into_mysql
from product_details import generate_product_details_data, insert_product_details_into_mysql
from categories import generate_category_data, insert_category_data_into_mysql
from Discount import generate_discount_data, insert_discount_data_into_mysql
from payment_mode import insert_payment_method_data_into_mysql
from customer import generate_customer_data, insert_customer_data_into_mysql
from customer_payment import generate_customer_payment_data, insert_customer_payment_data_into_mysql
from order_details import generate_order_data1, insert_order_data_into_mysql

def main():
    conn = None
    cursor = None
    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mycart"
        )
        
        cursor = conn.cursor()

        # Generate and insert data for registration
        num_registration = 50
        registration_data = generate_vendor_data(num_registration)
        insert_registration_into_mysql(registration_data)
        time.sleep(2)  # Delay for 2 seconds

        # Generate and insert data for vendor details
        vendor_details_data = generate_vendor_details_data(num_registration)
        insert_vendor_details_into_mysql(vendor_details_data, cursor, conn)
        time.sleep(2)  # Delay for 2 seconds

        # Generate and insert data for product details
        num_products = 50
        product_details_data = generate_product_details_data(num_products)
        insert_product_details_into_mysql(product_details_data, cursor, conn)
        time.sleep(2)  # Delay for 2 seconds

        # Generate and insert data for categories
        num_categories = 50
        category_data = generate_category_data(num_categories)
        insert_category_data_into_mysql(category_data, cursor, conn)
        time.sleep(2)  # Delay for 2 seconds

        # Generate and insert data for discounts
        num_discounts = 20
        discount_data = generate_discount_data(num_discounts)
        insert_discount_data_into_mysql(discount_data, cursor, conn)
        time.sleep(2)  # Delay for 2 seconds

        # Generate and insert data for payment methods
        insert_payment_method_data_into_mysql(cursor, conn)
        time.sleep(2)  # Delay for 2 seconds

        # Generate and insert data for customers
        num_customers = 50
        customer_data = generate_customer_data(num_customers)
        insert_customer_data_into_mysql(customer_data, cursor, conn)
        time.sleep(2)  # Delay for 2 seconds

        # Generate and insert data for customer payments
        num_customer_payments = 50
        customer_payment_data = generate_customer_payment_data(num_customer_payments)
        insert_customer_payment_data_into_mysql(customer_payment_data, cursor, conn)
        time.sleep(2)  # Delay for 2 seconds

        # Generate and insert data for orders
        num_orders = 50
        order_data = generate_order_data1(num_orders)
        insert_order_data_into_mysql(order_data, cursor, conn)
        time.sleep(2)  # Delay for 2 seconds

        # Close the database connection
        cursor.close()
        conn.close()

        # Print a message and exit the program
        print("All tables created successfully.")
        exit()

    except mysql.connector.Error as err:
        print("An error occurred:", err)
    finally:
        # Make sure to close the cursor and connection even if an exception occurs
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print("Cursor and connection closed.")

if __name__ == "__main__":
    main()





