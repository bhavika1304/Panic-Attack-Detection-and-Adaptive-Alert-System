import mysql.connector
from mysql.connector import Error

try:
    # Connect to the MySQL server
    connection = mysql.connector.connect(
        host="127.0.0.1",      # XAMPP MySQL server
        port=3307,             # XAMPP MySQL port (as configured in my.ini)
        user="root",           # Default username
        password="",           # Default password for root user (empty string)
        database="test_database"  # Replace with your database name
    )

    # Check if the connection is successful
    if connection.is_connected():
        print("Connected to the database")

        # Create a cursor object
        cursor = connection.cursor()

        # Example: Insert data into the 'users' table
        insert_query = "INSERT INTO users (username, email) VALUES (%s, %s)"
        user_data = [("Alice", "alice@example.com"), ("Bob", "bob@example.com")]

        cursor.executemany(insert_query, user_data)
        connection.commit()
        print(f"{cursor.rowcount} rows were inserted.")

        # Example: Fetch data from the 'users' table
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        print("Users in the database:")
        for row in rows:
            print(row)

except Error as e:
    print(f"Error: {e}")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
