import sqlite3
from models import Item, ItemCreate, ItemRemove, ItemUpdate

# Database configuration
database_path = "app/database/"
database_name = "shop_data.db"


def create_item_table():
    """Initialize items table."""
    try:
        with sqlite3.connect(database_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                    CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    price INTEGER NOT NULL)
                    """)
            return True
    except sqlite3.Error as e:
        print(f"資料庫操作發生錯誤: {e}")
        return False

def add_item(item : ItemCreate):
    """Add a new item to the database."""
    try:
        with sqlite3.connect(database_name) as conn:
            cursor = conn.cursor()
            # Directly insert the item. The UNIQUE constraint on 'name' will prevent duplicates.
            cursor.execute("INSERT INTO items (name, price) VALUES (?, ?)", (item.name, item.price))
            return True
    except sqlite3.Error as e:
        print(f"資料庫操作發生錯誤: {e}")
        return False

def remove_item(item : ItemRemove):
    """Remove an item from the database."""
    try:
        with sqlite3.connect(database_name) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM items WHERE id = ?", (item.id,))
            if cursor.rowcount == 0:
                print(f"Item with id {item.id} not found. Nothing removed.")
                return False
            return True
    except sqlite3.Error as e:
        print(f"資料庫操作發生錯誤: {e}")
        return False

def update_item(item : ItemUpdate):
    """Update an item in the database."""
    try:
        with sqlite3.connect(database_name) as conn:
            cursor = conn.cursor()
            # COALESCE is used to keep the existing value if the new value(item) is None.
            # If the value is not provided (None), it retains the current value in the database.
            cursor.execute("""
                UPDATE items 
                SET name = COALESCE(?, name), 
                    price = COALESCE(?, price) 
                WHERE id = ?
                """, (item.name, item.price, item.id)
            )
            if cursor.rowcount == 0:
                print(f"Item with id {item.id} not found. Nothing updated.")
                return False
            return True
    except sqlite3.IntegrityError as e:
        print(f"資料庫操作發生錯誤: {e}")
        return False

def get_item_list():
    """Retrieve a list of all items from the database."""
    try:
        with sqlite3.connect(database_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, price FROM items")
            itmes = cursor.fetchall()
            if itmes:
                return [Item(id=row[0], name=row[1], price=row[2]) for row in itmes]
            else:
                return []
    except sqlite3.Error as e:
        print(f"資料庫操作發生錯誤: {e}")
        return []

# Initialize the database and create the items table
create_item_table()
# Example usage for testing, should be removed or commented out in production code.
item1 = ItemCreate(name="Laptop", price=1500)
item2 = ItemCreate(name="Smartphone", price=800)
item3 = ItemCreate(name="Tablet", price=1200)
# add_item(item1)
add_item(item2)
add_item(item3)
print(get_item_list())