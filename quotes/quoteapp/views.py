from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Author, Quote
from .forms import AuthorForm, QuoteForm

def main(request, page=1):

    quotes = Quote.objects.all().order_by('-created_at')

    per_page = 10

    paginator = Paginator(quotes, per_page)

    quotes_on_page = paginator.get_page(page)

    return render(request, 'quoteapp/index.html', context={'quotes': quotes_on_page})

def author_detail(request, id_):

    author = get_object_or_404(Author, pk=id_)      

    return render(request, 'quoteapp/detail.html', context={'author': author})

@login_required
def add_author(request):

    if request.method == 'POST':

        form = AuthorForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(to='quoteapp:main')
        
        else:

            return render(request, 'quoteapp/author.html', {'form': form})

    return render(request, 'quoteapp/author.html', {'form': AuthorForm()})

@login_required
def add_quote(request):

    if request.method == 'POST':

        form = QuoteForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect(to='quoteapp:main')
        
        else:

            return render(request, 'quoteapp/quote.html', {'form': form})

    return render(request, 'quoteapp/quote.html', {'form': QuoteForm()})