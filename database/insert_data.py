import sqlite3
import pandas as pd

def insert_scraping_data(df: pd.DataFrame):
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

    print(f"🗃️ Number of lines in 'books' table: {rows[0][0]}\n")

def insert_api_request_data(df: pd.DataFrame):
    connection = sqlite3.connect('book_store.db')
    cursor = connection.cursor()

    # empecher les doublons
    def insert_books_without_duplicates(df_books: pd.DataFrame):
        books_currently_in_db = pd.read_sql('SELECT book_id FROM books', connection)
        new_books_only = df_books[
            # PAS les book_id qui sont dans books_currently_in_db
            ~df_books['book_id'].isin(books_currently_in_db['book_id'])
            ]

        if not new_books_only.empty:
            new_books_only.to_sql('books', con=connection, if_exists='append', index=False)
            print(f'📚 {len(new_books_only)} book(s) added.\n')
        else:
            print('😭 No new books added, none were found or all of them are already in the database.\n')

    insert_books_without_duplicates(df)
        
    # Vérifier que le nombre de livres dans la table correspond au nb de livres scrapés + livres de l'API
    cursor.execute('SELECT COUNT(*) FROM books')
    rows = cursor.fetchall()

    print(f"🗃️ Number of lines in 'books' table: {rows[0][0]}")