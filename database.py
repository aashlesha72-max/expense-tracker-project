import sqlite3

# Create connection
conn = sqlite3.connect("expenses.db")

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    category TEXT,
    date TEXT,
    description TEXT
)
""")

# Save and close
conn.commit()
conn.close()

print("Database and table created successfully!")