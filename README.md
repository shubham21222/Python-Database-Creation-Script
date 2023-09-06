# SQL Database Automation with Python

This repository contains Python scripts and resources to automate the process of creating SQL databases and populating them with tables and data. It simplifies the database setup process, making it faster and more convenient.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [conclusion](#conclusion)
## Introduction

Managing SQL databases can be a time-consuming task. This project aims to streamline the process by providing Python scripts that automate the creation of SQL databases, tables, and data population. Whether you're a developer, a system administrator, or someone who frequently sets up databases, this tool can save you valuable time.

## Features

- Automated SQL database creation.
- Customizable database configurations.
- Support for various SQL database systems (e.g., MySQL, PostgreSQL, SQLite).
- Easy-to-use command-line interface (CLI).
- Extensible for additional functionality.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- [Database system](#supported-database-systems) installed and running (if applicable).

## Project Structure

### `automation_database.py` Script

- `automation_database.py`: This script is the entry point of the automation process. It imports and executes individual scripts for each table creation and data population.

### Individual Scripts

- `sql_database.py`: Create and populate the Registration table.
- `account_details.py`: Create and populate the vendor details table.
- `product_details.py`: Create and populate the product details table.
- `categories.py`: Create and populate the category table.
- `Discount.py`: Create and populate the discount table.
- `payment_mode.py`: Create and populate the payment_mode table.
- `Customer.py`: Create and populate the Customer table.
- `customer_payment.py`: Create and populate the customer payment table.
- `order_details.py`: Create and populate the order details table.

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/SQL-DB-Automation.git


2. Install the required dependencies:

  ```bash
    pip install faker
    pip install mysql-connector-python
  ```
  
3. How to Run

   1.Ensure your PostgreSQL server is up and running.

   2.Navigate to the repository directory and execute the main script:

    ```bash
        python automation_database.py
    ```

This script automatically creates database tables and populates them with data using individual scripts.



## conclusion




This project showcases the power of automation in database setup and data population for a e-commarce website vendors functionality. By utilizing Python scripts, Faker library, and psycopg2, we have successfully streamlined the process, enabling consistent, efficient, and error-free database creation and population.





## Contributing
We welcome contributions from the community. If you find a bug or have an idea for improvement, please open an issue or submit a pull request. For more information, please read our Contributing Guidelines.




    This README provides users with clear instructions on how to list all tables in a database and then create additional tables using the provided Python scripts. Make sure to replace the placeholders with your actual project details.
