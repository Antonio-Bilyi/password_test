import json

from models import Authors
from quotes.utils.connect_to_mongo import connect_to_db
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

def load_authors(filepath):

    with open(filepath, 'r', encoding='utf-8') as file:

        data = json.load(file)

        for el in data:

            Authors(
                fullname = el.get('fullname'),
                born_date = el.get('born_date'),
                born_location = el.get('born_location'),
                description = el.get('description')
            ).save()
    
    print('Data successful loaded...')

if __name__ == '__main__':

    connect_to_db()
    load_authors('authors.json')