from pipelines import pipeline_scraping as ps
from pipelines import pipeline_api_request as pa
import argparse
import inquirer

def main():
    """
    Main function
    """
    try:
        parser = argparse.ArgumentParser(description='Scraping books from books.toscrape.com')
        
        # on définit l'argument --pages
        parser.add_argument(
            '--pages',
            type=int,
            help='Number of pages you want to scrape.'
        )

        # --pages devient args.pages
        args = parser.parse_args()
        ps.run_scraping_pipeline(args.pages)

        question = [inquirer.List('continue', message='Do you want to search for some more books through Google Books\' API', choices=['yes', 'no'])]

        answer = inquirer.prompt(question)
        if answer['continue'] == 'yes':
            pa.run_api_request_pipeline()
        else:
            print('Exiting...')

    # ^C
    except KeyboardInterrupt:
        print('User interrupted the program. Exiting...')
    # autres erreurs
    except Exception as e:
        print(f'An error occurred: {e}')

# éviter une exécution accidentelle (en cas d'import par ex)
if __name__ == '__main__':
    main()