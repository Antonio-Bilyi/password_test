from django import template
from utils.models import Authors

register = template.Library()

@register.filter(name='author')
def get_author(id_):

    author = Authors.objects(id=id_).first()

    return author['fullname']