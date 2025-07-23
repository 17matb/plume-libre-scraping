import sqlite3
import pandas as pd

# fonction permettant de créer une db, y insérer les données et afficher le nombre de livres de la base pour vérifier l'insertion
def insert_book_data(df: pd.DataFrame):
    connection = sqlite3.connect('book_store.db')

    df.to_sql(name='books', con=connection, if_exists='replace', index=False)

    cursor = connection.cursor()

    cursor.execute('SELECT COUNT(*) FROM books')
    rows = cursor.fetchall()

    for row in rows:
        print(row)