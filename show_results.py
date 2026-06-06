import sqlite3
from prettytable import PrettyTable  # pip install prettytable

def show_results():
    conn = sqlite3.connect("results.db")
    c = conn.cursor()

    # Create both tables if they don't exist
    c.execute('''CREATE TABLE IF NOT EXISTS image_results
                 (image_name TEXT, result TEXT, timestamp TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS text_results
                 (file_name TEXT, action TEXT, secret_preview TEXT, timestamp TEXT)''')

    # Fetch both types of results
    c.execute("SELECT * FROM image_results")
    image_rows = c.fetchall()

    c.execute("SELECT * FROM text_results")
    text_rows = c.fetchall()

    conn.close()

    print("\n================= 📸 IMAGE STEGANOGRAPHY RESULTS =================")
    if image_rows:
        table1 = PrettyTable()
        table1.field_names = ["Image Name", "Result", "Timestamp"]
        for row in image_rows:
            table1.add_row(row)
        print(table1)
    else:
        print("No image detection results yet.")

    print("\n================= ✉️ TEXT STEGANOGRAPHY RESULTS =================")
    if text_rows:
        table2 = PrettyTable()
        table2.field_names = ["File Name", "Action", "Message Preview", "Timestamp"]
        for row in text_rows:
            table2.add_row(row)
        print(table2)
    else:
        print("No text encoding/decoding results yet.")