import json

from models import Authors, Quotes
from quotes.utils.connect_to_mongo import connect_to_db
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

def load_quotes(filepath):

    with open(filepath, 'r', encoding='utf-8') as file:

        data = json.load(file)

        for el in data:

            author_name = el.get('author')
            author = Authors.objects(fullname=author_name).first()

            tags = [tag.strip().lower() for tag in el.get('tags', [])]

            Quotes(
                quote = el.get('quote'),
                author = author,
                tags = tags,
            ).save()
        
    print('Data successful loaded...')


if __name__ == '__main__':

    connect_to_db()
    load_quotes('quotes.json')