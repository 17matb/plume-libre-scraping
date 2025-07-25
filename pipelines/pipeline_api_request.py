import os, sys

# sys.path : liste des chemins où python va chercher les modules
# insert(0, chemin) on place le chemin en première position
# et on récupère le dirname du dirname du fichier actuel (variable __file__)
# résultat : on peut import les modules depuis la racine du projet
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from get_data import get_api_request_data
from process_data import process_api_request_data
from database import insert_data
import pandas as pd
import inquirer

def run_api_request_pipeline():
    filterList = ['partial', 'full', 'free-ebooks', 'paid-ebooks', 'ebooks']
    maxResultsList = [10, 20, 30, 40]
    orderByList = ['relevance', 'newest']

    questions = [
        inquirer.Text('q', message='What would you like to search?'),
        inquirer.List('filter', message='Select a filter', choices=filterList),
        inquirer.List('maxResults', message='Maximum results', choices=maxResultsList),
        inquirer.List('orderBy', message='Order results by', choices=orderByList),
    ]

    answers = inquirer.prompt(questions)

    q = answers['q']
    filter = answers['filter']
    maxResults = answers['maxResults']
    orderBy = answers['orderBy']

    print('👀 Fetching data...\n')

    api_request_data = get_api_request_data.get_api_request_data(q, filter, maxResults, orderBy)
    processed_data = process_api_request_data.process_api_request_data(api_request_data)

    insert_data.insert_api_request_data(processed_data)

# run_api_request_pipeline()