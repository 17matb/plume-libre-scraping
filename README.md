# Scraping de données

## Quel est l'objectif du projet ?

Scrape des informations sur des livres depuis https://books.toscrape.com et les stocker dans une base de donnée SQLite.

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

### Simple :

```bash
python main.py
```

### Option pages :

```bash
python main.py --pages <nombre de pages à scrape>
```

Exemple :

```bash
python main.py --pages 10
```
