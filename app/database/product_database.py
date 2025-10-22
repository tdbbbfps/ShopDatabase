import sqlite3
from models.product import Product, productCreate, productRemove, productUpdate

# Database configuration
database_path = "app/database/shop_data.db"


def create_product_table():
    """Initialize products table."""
    try:
        with sqlite3.connect(database_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                    CREATE TABLE IF NOT EXISTS products (
                    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    price INTEGER NOT NULL,
                    quantity INTEGER NOT NULL)
                    """)
            return True
    except sqlite3.Error as e:
        print(f"資料庫操作發生錯誤: {e}")
        return False

def add_product(product : ProductCreate):
    """Add a new product to the database."""
    try:
        with sqlite3.connect(database_path) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", (product.name, product.price, product.quantity))
            return True
    except sqlite3.Error as e:
        print(f"資料庫操作發生錯誤: {e}")
        return False

def remove_product(product : ProductRemove):
    """Remove an product from the database."""
    try:
        with sqlite3.connect(database_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM products WHERE product_id = ?", (product.product_id ,))
            if cursor.rowcount == 0:
                print(f"product with product_id {product.product_idid} not found. Nothing removed.")
                return False
            return True
    except sqlite3.Error as e:
        print(f"資料庫操作發生錯誤: {e}")
        return False

def update_product(product : ProductUpdate):
    """Update an product in the database."""
    try:
        with sqlite3.connect(database_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE products 
                SET name = ?, 
                    price = ? 
                WHERE product_id = ?
                """, (product.name, product.price, product.product_id ))
    except sqlite3.Error as e:
        print(f"資料庫操作發生錯誤: {e}")
        return False

def update_product(product : ProductUpdate):
    """Update an product in the database."""
    try:
        with sqlite3.connect(database_path) as conn:
            cursor = conn.cursor()
            # COALESCE is used to keep the existing value if the new value(product) is None.
            # If the value is not provided (None), it retains the current value in the database.
            cursor.execute("""
                UPDATE products 
                SET name = COALESCE(?, name), 
                    price = COALESCE(?, price) 
                WHERE product_id = ?
                """, (product.name, product.price, product.product_id )
            )
            if cursor.rowcount == 0:
                print(f"product with product_id {product.product_id } not found. Nothing updated.")
                return False
            return True
    except sqlite3.IntegrityError as e:
        print(f"資料庫操作發生錯誤: {e}")
        return False

def get_product_list():
    """Retrieve a list of all products from the database."""
    try:
        with sqlite3.connect(database_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT product_id , name, price FROM products")
            itmes = cursor.fetchall()
            if itmes:
                return [product(id=row[0], name=row[1], price=row[2]) for row in itmes]
            else:
                return []
    except sqlite3.Error as e:
        print(f"資料庫操作發生錯誤: {e}")
        return []

# Initialize the database and create the products table
create_product_table()
# Example usage for testing, should be removed or commented out in production code.
product1 = ProductCreate(name="Laptop", price=1500)
product2 = ProductCreate(name="Smartphone", price=800)
product3 = ProductCreate(name="Tablet", price=1200)
# add_product(product1)
add_product(product2)
add_product(product3)
print(get_product_list())