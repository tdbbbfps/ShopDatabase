import sqlite3
# 每一筆交易共用一個sales_id，分別存入每樣商品、商品總價格與時間戳記
def create_sale_table():
    """Initialize sales table."""
    try:
        with sqlite3.connect(database_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                    CREATE TABLE IF NOT EXISTS sales (
                    sales_id INTEGER,
                    products TEXT NOT NULL,
                    quantity INTEGER NOT NULL,
                    total_price INTEGER NOT NULL
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)
                    )""")
            return True
    except sqlite3.Error as e:
        print(f"資料庫操作發生錯誤: {e}")
        return False

def add_sales()