from django.urls import path

from . import views

app_name = 'quoteapp'

urlpatterns = [
    path('', views.main, name = 'main'),
    path('<int:page>', views.main, name = 'root_pagination'),
    path('author/add', views.add_author, name = 'add-author'),
    path('author/<int:id_>', views.author_detail, name = 'detail'),
    path('quote/add', views.add_quote, name = 'add-quote'),
]