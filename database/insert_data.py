import sqlite3
import pandas as pd

def insert_data(df: pd.DataFrame):
    """
    Create a database, insert book data and display the number of inserted books for verification.

    Args:
        df (pd.DataFrame): The DataFrame containing the book data to insert.

    Returns:
        none
    """
    connection = sqlite3.connect('book_store.db')

    df.to_sql(name='books', con=connection, if_exists='replace', index=False)

    cursor = connection.cursor()

    cursor.execute('SELECT COUNT(*) FROM books')
    rows = cursor.fetchall()

    print(f"🗃️ Number of lines in 'books' table: {rows[0][0]}")