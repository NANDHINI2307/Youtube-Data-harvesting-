# database/mysql.py
import mysql.connector

# MySQL connection configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "white",
    "database": "youtube_app",
}

def migrate_channel_data_to_mysql(channel_data):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Migrate channel data to MySQL
        # Replace with your actual SQL statements

        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

def search_data_in_mysql(field, query):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Perform a search query
        # Replace with your actual SQL SELECT statement

        result = cursor.fetchall()
        return result
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()
