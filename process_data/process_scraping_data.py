import pandas as pd

def process_scraping_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Process data, convert the types of the DataFrame to appropriate types.

    Args:
        df (pd.DataFrame): The DataFrame to process.

    Returns:
        pd.DataFrame: Processed DataFrame.
    """
    processed_df = df.copy()

    def convert_availability(value : str) -> bool:
        """Convert the availability value to a boolean.

        Args:
            value (str): The availability status of the book.

        Returns:
            bool: True if the book is available, False otherwise.
        """
        if value == 'In stock':
            return True
        else:
            return False

    def convert_types(df_books: pd.DataFrame) -> pd.DataFrame:
        """Convert the types of the DataFrame columns to appropriate types.

        Args:
            df_books (pd.DataFrame): The DataFrame containing book data.

        Returns:
            pd.DataFrame: The DataFrame with converted types.
        """
        # Conversion de title en chaîne de caractères
        df_books["title"] = df_books['title'].astype('string')

        if df_books['price'].dtype != 'float64':
            df_books["price"] = df_books['price'].str[1:]
            # Convertir la colonne price en type décimal
            df_books["price"] = df_books['price'].astype('float64')

        # Convertir la colonne availability en booléen (True/False)
        if df_books['availability'].dtype != 'bool':
            df_books["availability"] = df_books['availability'].apply(convert_availability)
        
        ratings_map = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
        }

        if df_books['rating'].dtype != 'int':
            df_books["rating"] = df_books['rating'].map(ratings_map)

    convert_types(processed_df)

    return processed_df

# test
# test = pd.read_csv('./notebooks/books_infos.csv')
# print(test.head())
# test = process_scraping_data(test)
# print(test.head())