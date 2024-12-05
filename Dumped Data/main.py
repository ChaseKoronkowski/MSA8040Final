import flet as ft
import mysql.connector
from mysql.connector import Error
import base64
import os
import csv

# Database connection function
def get_db_connection():
    try:
        cnx = mysql.connector.connect(
            user='root',
            password='password',
            host='127.0.0.1',
            database='orion_stores'
        )
        return cnx
    except Error as e:
        print(f"Error: {e}")
        return None

# Create customer_reviews table
def create_customer_reviews_table():
    cnx = get_db_connection()
    if cnx:
        try:
            cursor = cnx.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS `orion_stores`.`customer_reviews` (
                    `Review_ID` INT NOT NULL AUTO_INCREMENT,
                    `Product_ID` INT NOT NULL,
                    `Employee_Name` VARCHAR(255) NOT NULL,
                    `Review_Text` TEXT NOT NULL,
                    `Rating` INT NOT NULL,
                    `Review_Date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    PRIMARY KEY (`Review_ID`),
                    FOREIGN KEY (`Product_ID`) REFERENCES `orion_stores`.`product_dim`(`Product_ID`) ON DELETE CASCADE ON UPDATE CASCADE
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
                """
            )
            cnx.commit()
            print("customer_reviews table created successfully!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if cnx.is_connected():
                cnx.close()

# Basic CRUD queries for the database

# CREATE - Add new record

def create_customer(customer_id, name, country, gender):
    cnx = get_db_connection()
    if cnx:
        try:
            cursor = cnx.cursor()
            cursor.execute(
                "INSERT INTO customer (Customer_ID, Employee_Name, Country, Gender) VALUES (%s, %s, %s, %s)",
                (customer_id, name, country, gender)
            )
            cnx.commit()
            print("Customer added successfully!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if cnx.is_connected():
                cnx.close()

# READ - Fetch specific record

def read_customer(customer_id):
    cnx = get_db_connection()
    if cnx:
        try:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM customer WHERE Customer_ID = %s", (customer_id,))
            customer = cursor.fetchone()
            return customer
        except Error as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if cnx.is_connected():
                cnx.close()
    return None

# UPDATE - Update existing record

def update_customer(customer_id, name=None, country=None, gender=None):
    cnx = get_db_connection()
    if cnx:
        try:
            cursor = cnx.cursor()
            updates = []
            values = []

            if name is not None:
                updates.append("Employee_Name = %s")
                values.append(name)
            if country is not None:
                updates.append("Country = %s")
                values.append(country)
            if gender is not None:
                updates.append("Gender = %s")
                values.append(gender)

            if updates:
                values.append(customer_id)
                update_query = f"UPDATE customer SET {', '.join(updates)} WHERE Customer_ID = %s"
                cursor.execute(update_query, tuple(values))
                cnx.commit()
                print("Customer updated successfully!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if cnx.is_connected():
                cnx.close()

# DELETE - Remove record from the database

def delete_customer(customer_id):
    cnx = get_db_connection()
    if cnx:
        try:
            cursor = cnx.cursor()
            cursor.execute("DELETE FROM customer WHERE Customer_ID = %s", (customer_id,))
            cnx.commit()
            print("Customer deleted successfully!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if cnx.is_connected():
                cnx.close()

# Product browsing function
def fetch_product_details(product_id):
    cnx = get_db_connection()
    if cnx:
        try:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM product_dim WHERE `Product_ID` = %s", (product_id,))
            product = cursor.fetchone()
            return product
        except Error as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if cnx.is_connected():
                cnx.close()


def fetch_products_by_category(category):
    cnx = get_db_connection()
    if cnx:
        try:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT p.`Product_ID` AS Product_ID, p.Product_Name, pr.Unit_Price FROM product_dim p LEFT JOIN prices pr ON p.`Product_ID` = pr.`Product_ID` WHERE p.Product_Category = %s", (category,))
            products = cursor.fetchall()
            return products
        except Error as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if cnx.is_connected():
                cnx.close()
    return []

# Order processing function
def process_order(order_id, customer_id, product_id, employee_id, street_id, order_date, delivery_date, order_type, quantity, total_retail_price, cost_price, discount):
    cnx = get_db_connection()
    if cnx:
        try:
            cursor = cnx.cursor()
            cursor.execute(
                "INSERT INTO order_fact (Order_ID, Customer_ID, Product_ID, Employee_ID, Street_ID, Order_Date, Delivery_Date, Order_Type, Quantity, Total_Retail_Price, CostPrice_Per_Unit, Discount) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (order_id, customer_id, product_id, employee_id, street_id, order_date, delivery_date, order_type, quantity, total_retail_price, cost_price, discount)
            )
            cnx.commit()
            print("Order successfully processed!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if cnx.is_connected():
                cnx.close()

# Customer review submission function
def submit_customer_review(product_id, customer_name, review_text, rating):
    cnx = get_db_connection()
    if cnx:
        try:
            cursor = cnx.cursor()
            cursor.execute(
                "INSERT INTO customer_reviews (Product_ID, Employee_Name, Review_Text, Rating) VALUES (%s, %s, %s, %s)",
                (product_id, customer_name, review_text, rating)
            )
            cnx.commit()
            print("Review successfully submitted!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if cnx.is_connected():
                cnx.close()

# HR functionality
def fetch_employee_details(employee_id):
    cnx = get_db_connection()
    if cnx:
        try:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM staff WHERE Employee_ID = %s", (employee_id,))
            employee = cursor.fetchone()
            if employee:
                cursor.execute("SELECT * FROM employee_organization WHERE Employee_ID = %s", (employee_id,))
                organization_details = cursor.fetchone()
                employee.update(organization_details if organization_details else {})
            return employee
        except Error as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if cnx.is_connected():
                cnx.close()
    return None


def fetch_all_employees():
    cnx = get_db_connection()
    if cnx:
        try:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT Employee_ID, Employee_Name FROM staff")
            employees = cursor.fetchall()
            return employees
        except Error as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if cnx.is_connected():
                cnx.close()
    return []


def add_new_employee(employee_data):
    cnx = get_db_connection()
    if cnx:
        try:
            cursor = cnx.cursor()
            cursor.execute(
                "INSERT INTO staff (Employee_ID, Employee_Name, Job_Title, Salary, Gender, Birth_Date, Emp_Hire_Date) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (employee_data['Employee_ID'], employee_data['Employee_Name'], employee_data['Job_Title'],
                 employee_data['Salary'], employee_data['Gender'], employee_data['Birth_Date'],
                 employee_data['Emp_Hire_Date'])
            )
            cnx.commit()
            print("Employee successfully added!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if cnx.is_connected():
                cnx.close()


def add_new_product(product_data):
    cnx = get_db_connection()
    if cnx:
        try:
            cursor = cnx.cursor()
            cursor.execute(
                "INSERT INTO product_dim (Product_ID, Product_Name, Product_Line, Product_Category, Product_Group, Supplier_Country, Supplier_Name, Supplier_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (product_data['Product_ID'], product_data['Product_Name'], product_data['Product_Line'],
                 product_data['Product_Category'], product_data['Product_Group'], product_data['Supplier_Country'],
                 product_data['Supplier_Name'], product_data['Supplier_ID'])
            )
            cnx.commit()
            print("Product successfully added!")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if cnx.is_connected():
                cnx.close()

# Export table to CSV
from datetime import datetime

def export_table_to_csv(query, filename):
    cnx = get_db_connection()
    if cnx:
        try:
            cursor = cnx.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            headers = [i[0] for i in cursor.description]

            downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_path = os.path.join(downloads_path, f"{filename}_{timestamp}.csv")

            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(rows)

            print(f"File successfully saved to {file_path}")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if cnx.is_connected():
                cnx.close()

# Flet UI
def fetch_unique_categories():
    cnx = get_db_connection()
    if cnx:
        try:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT DISTINCT Product_Category FROM product_dim")
            categories = cursor.fetchall()
            return [category['Product_Category'] for category in categories]
        except Error as e:
            print(f"Error: {e}")
        finally:
            if cursor:
                cursor.close()
            if cnx.is_connected():
                cnx.close()
    return []


def open_add_order_view(e, page):
    order_id_input.visible = True
    customer_id_input.visible = True
    product_id_input_order.visible = True
    employee_id_input_order.visible = True
    street_id_input.visible = True
    order_date_input.visible = True
    delivery_date_input.visible = True
    order_type_input.visible = True
    order_quantity_input.visible = True
    total_retail_price_input.visible = True
    cost_price_input.visible = True
    discount_input.visible = True
    page.update()

order_id_input = ft.TextField(label="Order ID", width=200, visible=False)
customer_id_input = ft.TextField(label="Customer ID", width=200, visible=False)
product_id_input_order = ft.TextField(label="Product ID", width=200, visible=False)
employee_id_input_order = ft.TextField(label="Employee ID", width=200, visible=False)
street_id_input = ft.TextField(label="Street ID", width=200, visible=False)
order_date_input = ft.TextField(label="Order Date (YYYY-MM-DD)", width=200, visible=False)
delivery_date_input = ft.TextField(label="Delivery Date (YYYY-MM-DD)", width=200, visible=False)
order_type_input = ft.TextField(label="Order Type", width=200, visible=False)
order_quantity_input = ft.TextField(label="Quantity", width=200, visible=False)
total_retail_price_input = ft.TextField(label="Total Retail Price", width=200, visible=False)
cost_price_input = ft.TextField(label="Cost Price Per Unit", width=200, visible=False)
discount_input = ft.TextField(label="Discount", width=200, visible=False)

def main(page: ft.Page):
    page.title = "Orion Stores - E-Commerce Platform"
    page.scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.DARK  # Enable dark theme

    # Create customer_reviews table
    create_customer_reviews_table()

    # Product browsing UI
    product_id_input = ft.TextField(label="Product ID", width=300)
    product_details_output = ft.Text()

    category_dropdown = ft.Dropdown(label="Product Category", width=300, options=[ft.dropdown.Option(category) for category in fetch_unique_categories()])
    product_list_view = ft.ListView(expand=True, spacing=10)

    def on_category_select(e):
        category = category_dropdown.value
        products = fetch_products_by_category(category)
        product_list_view.controls = [ft.Text(f"{product['Product_Name']} (ID: {product['Product_ID']}, Price: {product.get('Product_Line', 'N/A')})") for product in products]
        page.update()

    def on_product_search(e):
        product_id = product_id_input.value
        product_details = fetch_product_details(product_id)
        if product_details:
            product_details_output.value = f"Product Name: {product_details['Product_Name']}, Price: {product_details['Product_Line']}, Supplier: {product_details['Supplier_Name']}"
        else:
            product_details_output.value = "Product not found"
        page.update()

    category_search_button = ft.ElevatedButton("Search by Category", on_click=on_category_select)
    product_search_button = ft.ElevatedButton("Search Product", on_click=on_product_search)
    export_products_button = ft.ElevatedButton("Export Products", on_click=lambda e: export_table_to_csv("SELECT * FROM product_dim", "products.csv"))

    # Order processing UI
    def on_order_process(e):
        order_id = order_id_input.value
        customer_id = customer_id_input.value
        product_id = product_id_input_order.value
        employee_id = employee_id_input_order.value
        street_id = street_id_input.value
        order_date = order_date_input.value
        delivery_date = delivery_date_input.value
        order_type = order_type_input.value
        quantity = order_quantity_input.value
        total_retail_price = total_retail_price_input.value
        cost_price = cost_price_input.value
        discount = discount_input.value
        process_order(order_id, customer_id, product_id, employee_id, street_id, order_date, delivery_date, order_type, quantity, total_retail_price, cost_price, discount)
        page.overlay.append(ft.SnackBar(ft.Text("Order successfully processed!"), open=True))
        page.update()

    order_process_button = ft.ElevatedButton("Process Order", on_click=on_order_process)
    add_order_button = ft.ElevatedButton("Add New Order", on_click=lambda e: open_add_order_view(e, page))
    export_orders_button = ft.ElevatedButton("Export Orders", on_click=lambda e: export_table_to_csv("SELECT * FROM order_fact", "orders.csv"))

    # Customer review UI
    review_text_input = ft.TextField(label="Review Text", width=400)
    customer_name_input = ft.TextField(label="Customer Name", width=200)
    rating_input = ft.TextField(label="Rating (1-10)", width=200)

    def on_review_submit(e):
        product_id = product_id_input.value
        customer_name = customer_name_input.value
        review_text = review_text_input.value
        rating = rating_input.value
        submit_customer_review(product_id, customer_name, review_text, rating)
        page.overlay.append(ft.SnackBar(ft.Text("Review successfully submitted!"), open=True))
        page.update()

    review_submit_button = ft.ElevatedButton("Submit Review", on_click=on_review_submit)
    export_reviews_button = ft.ElevatedButton("Export Reviews", on_click=lambda e: export_table_to_csv("SELECT * FROM customer_reviews", "customer_reviews_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".csv"))

    # HR functionality UI
    employee_id_input = ft.TextField(label="Employee ID", width=200)
    employee_details_output = ft.Text()
    employee_dropdown = ft.Dropdown(label="Employees", width=200)
    employee_list_view = ft.ListView(expand=True, spacing=10)

    def on_employee_search(e):
        employee_id = employee_id_input.value
        employee_details = fetch_employee_details(employee_id)
        if employee_details:
            employee_details_output.value = (
                f"Name: {employee_details['Employee_Name']}, Job Title: {employee_details['Job_Title']}, Salary: {employee_details['Salary']}, "
                f"Department: {employee_details.get('Department', 'N/A')}, Manager ID: {employee_details.get('Manager_ID', 'N/A')}"
            )
        else:
            employee_details_output.value = "Employee not found"
        page.update()

    def on_employee_dropdown_select(e):
        employee_id = employee_dropdown.value
        employee_id_input.value = employee_id
        on_employee_search(e)

    def on_load_employees(e):
        employees = fetch_all_employees()
        employee_list_view.controls = [ft.Text(f"{emp['Employee_Name']} (ID: {emp['Employee_ID']})") for emp in employees]
        page.update()

    employee_search_button = ft.ElevatedButton("Search Employee", on_click=on_employee_search)
    load_employees_button = ft.ElevatedButton("Load Employees", on_click=on_load_employees)
    employee_dropdown.on_change = on_employee_dropdown_select

    # Add new employee button in HR section
    def open_add_employee_menu(e):
        new_employee_id_input = ft.TextField(label="New Employee ID", width=200)
        new_employee_name_input = ft.TextField(label="Employee Name", width=200)
        new_employee_job_title_input = ft.TextField(label="Job Title", width=200)
        new_employee_salary_input = ft.TextField(label="Salary", width=200)
        new_employee_gender_input = ft.TextField(label="Gender", width=200)
        new_employee_birth_date_input = ft.TextField(label="Birth Date (YYYY-MM-DD)", width=200)
        new_employee_hire_date_input = ft.TextField(label="Hire Date (YYYY-MM-DD)", width=200)

        def on_add_employee(e):
            employee_data = {
                'Employee_ID': new_employee_id_input.value,
                'Employee_Name': new_employee_name_input.value,
                'Job_Title': new_employee_job_title_input.value,
                'Salary': new_employee_salary_input.value,
                'Gender': new_employee_gender_input.value,
                'Birth_Date': new_employee_birth_date_input.value,
                'Emp_Hire_Date': new_employee_hire_date_input.value
            }
            add_new_employee(employee_data)
            page.overlay.append(ft.SnackBar(ft.Text("Employee successfully added!"), open=True))
            page.update()

        add_employee_button = ft.ElevatedButton("Add Employee", on_click=on_add_employee)

        # Open a new window for adding employee
        dialog = ft.AlertDialog(
            title=ft.Text("Add New Employee"),
            content=ft.Column([
                new_employee_id_input,
                new_employee_name_input,
                new_employee_job_title_input,
                new_employee_salary_input,
                new_employee_gender_input,
                new_employee_birth_date_input,
                new_employee_hire_date_input,
                add_employee_button
            ]),
            on_dismiss=lambda e: print("Add Employee dialog closed")
        )
        page.dialog = dialog
        dialog.open = True
        page.update()

    add_employee_menu_button = ft.ElevatedButton("Add New Employee", on_click=open_add_employee_menu)

    # Adding elements to the page
    page.add(
        ft.Column([
            ft.Text("Product Browsing", style="headline6"),
            category_dropdown,
            category_search_button,
            product_list_view,
            product_id_input,
            product_search_button,
            export_products_button,
            product_details_output,
            ft.Divider(),
            ft.Text("Order Processing", style="headline6"),
            add_order_button,
            order_id_input,
            customer_id_input,
            product_id_input_order,
            employee_id_input_order,
            street_id_input,
            order_date_input,
            delivery_date_input,
            order_type_input,
            order_quantity_input,
            total_retail_price_input,
            cost_price_input,
            discount_input,
            order_process_button,
            export_orders_button,
            ft.Divider(),
            ft.Text("Customer Reviews", style="headline6"),
            customer_name_input,
            review_text_input,
            rating_input,
            review_submit_button,
            export_reviews_button,
            ft.Divider(),
            ft.Text("HR Functionality", style="headline6"),
            employee_id_input,
            employee_search_button,
            employee_dropdown,
            load_employees_button,
            employee_list_view,
            employee_details_output,
            add_employee_menu_button
        ])
    )

ft.app(target=main)
