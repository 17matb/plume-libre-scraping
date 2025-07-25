import os, sys

# sys.path : liste des chemins où python va chercher les modules
# insert(0, chemin) on place le chemin en première position
# et on récupère le dirname du dirname du fichier actuel (variable __file__)
# résultat : on peut import les modules depuis la racine du projet
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from get_data import get_scraping_data
from process_data import process_scraping_data
from database import insert_data
import pandas as pd

def run_scraping_pipeline(pages = None):
    """Running scraping pipeline

    Args:
        pages (int, optional): Number of pages to scrape. If none, ask user.

    Returns:
        - (-): -
    """

    if pages is None:
        number_of_pages_to_scrape = int(input('📄 How many pages do you want to scrape?\n'))
    else:
        number_of_pages_to_scrape = pages

    print('\n👀 Scraping data...\n')
    scrape_result = get_scraping_data.scrape_books(number_of_pages_to_scrape)
    df_scrape = pd.DataFrame(scrape_result)

    print('📕 Here is your raw dataframe:\n')
    print(f'{df_scrape.head()}\n')

    df_scrape.to_csv('data/data_scraping.csv', index=False)
    df_scrape_processed = process_scraping_data.process_scraping_data(df_scrape)

    print('📘 Here is your processed dataframe:\n')
    print(f'{df_scrape_processed.head()}\n')

    print('👀 Creating db and inserting data...\n')
    insert_data.insert_scraping_data(df_scrape_processed)

# test
# run_scraping_pipeline()