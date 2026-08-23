from mongoengine import Document
from mongoengine.fields import StringField, EmailField, BooleanField, ListField, ReferenceField

class Authors(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()
    meta = {
        'indexes': ['fullname'],
        'collection': 'authors'
    }

class Quotes(Document):
    quote = StringField()
    author = ReferenceField(Authors)
    tags = ListField(StringField())
    meta = {
        'indexes': ['tags', 'author'],
        'collection': 'quotes'
    }