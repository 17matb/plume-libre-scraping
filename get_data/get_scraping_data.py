import requests
from bs4 import BeautifulSoup
import hashlib

def create_book_id(title, price):
    # on hash le titre et le prix pour obtenir un résultat proche des identifiants google books
    id = hashlib.md5((title + str(price)).encode('utf-8')).hexdigest()[:12]
    return id

def get_books_html(url: str) -> BeautifulSoup:
    """Fetch the HTML content of a book page.

    Args:
        url (str): The URL of the book page.

    Returns:
        BeautifulSoup: A BeautifulSoup object containing the HTML content.
    """
    response = requests.get(url)

    # On stocke le contenu HTML dans une variable
    html_content = response.content

    # On crée un objet BeautifulSoup pour parser le HTML
    soup = BeautifulSoup(html_content, "html.parser")

    return soup

# Parcourir les pages et récupérer les livres
def scrape_books(pages: int) -> list[dict]:
    """Scrape books from the specified number of pages.

    Args:
        pages (int): The number of pages to scrape.

    Returns:
        list: A list of dictionaries containing books information.
    """
    if pages <= 0:
        page_nb = 1
    else:
        page_nb = pages

    data_books = []

    for i in range(1, page_nb + 1):
        base_url = f'http://books.toscrape.com/catalogue/page-{i}.html'
        soup = get_books_html(base_url)
        books = soup.find_all("article", class_="product_pod")
        for j in books:
            book = extract_book_info(j)
            data_books.append(book)

    return data_books

# Fonction pour extraire le titre d'un livre
def extract_title(book: BeautifulSoup) -> str:
    """Extract the title of a book from a BeautifulSoup object.

    Args:
        book (BeautifulSoup): The HTML element of the book.

    Returns:
        str: The title of the book.
    """
    title = book.find('h3').find('a').get('title')

    return title

# Fonction pour extraire le prix d'un livre
def extract_price(book: BeautifulSoup) -> str:
    """Extract the price of a book from a BeautifulSoup object.

    Args:
        book (BeautifulSoup): The HTML element of the book.

    Returns:
        str: The price of the book.
    """
    price = book.find('div', class_='product_price').find('p', class_='price_color').text

    return price

# Fonction pour extraire la note d'un livre
def extract_rating(book: BeautifulSoup) -> str:
    """Extract the rating of a book from a BeautifulSoup object.

    Args:
        book (BeautifulSoup): The HTML element of the book.

    Returns:
        str: The rating of the book.
    """
    rating = book.find('p', class_='star-rating').get('class')[1]

    return rating

# Fonction pour extraire la disponibilité d'un livre
def extract_availability(book: BeautifulSoup) -> str:
    """Extract the availability of a book from a BeautifulSoup object.

    Args:
        book (BeautifulSoup): The HTML element of the book.

    Returns:
        str: The availability of the book.
    """
    availability = book.find('div', class_='product_price').find('p', class_='availability').text.strip()

    return availability

# Fonction qui combine les informations d'un livre dans un dictionnaire
def extract_book_info(book: BeautifulSoup) -> dict:
    """Extract all information of a book from a BeautifulSoup object.

    Args:
        book (BeautifulSoup): The HTML element of the book.

    Returns:
        dict: A dictionary containing the title, price, rating, and availability of the book.
    """
    book_info = {
        'book_id': create_book_id(extract_title(book), extract_price(book)), # ajout d'un book_id pour gérer efficacement l'absence de doublons
        'title': extract_title(book),
        'price': extract_price(book),
        'rating': extract_rating(book),
        'availability': extract_availability(book)
    }

    return book_info

