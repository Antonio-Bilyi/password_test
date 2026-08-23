import os
import django
from utils.connect_to_mongo import connect_to_db

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotes.settings')
django.setup()

from quoteapp.models import Author, Tag, Quote
from utils.models import Authors, Quotes


def migrate_authors() -> None:

    count = 0

    for author in Authors.objects.all():
        _, created = Author.objects.get_or_create(
            fullname=author.fullname,
            defaults={
                'born_date': author.born_date,
                'born_location': author.born_location,
                'description': author.description,
            }
        )
        if created:
            count += 1


def get_or_create_tags(tag_names: list[str]) -> list[Tag]:

    return [Tag.objects.get_or_create(name=tag_name)[0] for tag_name in tag_names]


def migrate_quotes() -> None:

    created_count = 0
    skipped_no_author = 0
    skipped_duplicate = 0

    for quote in Quotes.objects.all():

        if Quote.objects.filter(quote=quote.quote).exists():
            skipped_duplicate += 1
            continue

        if quote.author is None:
            print(f"Пропущено (немає автора): {quote.quote[:50]}")
            skipped_no_author += 1
            continue

        author = Author.objects.filter(fullname=quote.author.fullname).first()

        if author is None:
            print(f"Автора не знайдено в PostgreSQL: {quote.author.fullname}")
            skipped_no_author += 1
            continue

        tags = get_or_create_tags(quote.tags)

        new_quote = Quote.objects.create(
            quote=quote.quote,
            author=author,
        )
        new_quote.tags.set(tags)

        created_count += 1


if __name__ == '__main__':
    connect_to_db()
    migrate_authors()
    migrate_quotes()
    print("Міграція завершена.")