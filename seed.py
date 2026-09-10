import sqlite3

# This creates a file named 'cars.db' right inside your folder
connection = sqlite3.connect("cars.db")
cursor = connection.cursor()

# Create a table to store our cars
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS vehicles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand TEXT,
        model TEXT,
        price INTEGER,
        fuel_type TEXT,
        kilometers INTEGER
    )
"""
)

# Add some starter cars
sample_cars = [
    ("Hyundai", "Creta", 1400000, "Diesel", 45000),
    ("Maruti", "Swift", 650000, "Petrol", 20000),
    ("Tata", "Nexon", 1200000, "Diesel", 30000),
    ("Honda", "City", 1100000, "Petrol", 15000),
    ("Mahindra", "Scorpio", 1800000, "Diesel", 60000),
    ("Toyota", "Fortuner", 3200000, "Diesel", 50000),
    ("Hyundai", "i20", 800000, "Petrol", 10000),
    ("Kia", "Seltos", 1500000, "Diesel", 25000),
]

cursor.executemany(
    """
    INSERT INTO vehicles (brand, model, price, fuel_type, kilometers)
    VALUES (?, ?, ?, ?, ?)
""",
    sample_cars,
)

connection.commit()
connection.close()
print("Yay! Your database is created and filled with cars!")