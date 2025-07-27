import requests
import pandas as pd

def get_book_info(book):
    # utilisation de {} en guise de value car le défaut None n'a pas de méthode get() donc on utilise un dictionnaire vide pour continuer l'enchainement
    book_title = book.get('volumeInfo', {}).get('title')
    book_price = book.get('saleInfo', {}).get('listPrice', {}).get('amount')
    book_average_rating = book.get('volumeInfo', {}).get('averageRating')
    # on récupère l'id pour mieux gérer l'absence de doublons
    book_id = book.get('id')

    book_info = {
        'book_id': book_id,
        'title': book_title,
        'price': book_price,
        'rating': book_average_rating
    }

    return book_info

def get_api_request_data(q = 'food', filter='paid-ebooks', maxResults = 40, orderBy = 'relevance'):
    # URL de l'API Google Books
    url = 'https://www.googleapis.com/books/v1/volumes'

    params = {
    'q': q,
    'filter': filter,
    'maxResults': maxResults,
    'orderBy': orderBy
    }

    response = requests.get(url, params=params)
    # print(response.url)

    # Vérifier le code de statut de la réponse
    response.raise_for_status()
    # print(response)

    # Récupérer le coeur de la réponse
    data_books_raw = response.json()

    # Afficher les données récupérées
    # print(data_books_raw)

    data_books = data_books_raw.get('items')

    book_list = [get_book_info(i) for i in data_books]

    df_book_list = pd.DataFrame(book_list)

    return df_book_list

#test
# get_api_request_data()
