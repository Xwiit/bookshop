from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from . models import BookReview, Bookstore, Cart, Order

# Create your views here.

def index(request):
    #Fetching data from the database
    books = Bookstore.objects.all()

    #search coode
    book_or_author = request.GET.get('book_or_author')
    if book_or_author != '' and book_or_author is not None:
        books = Bookstore.objects.filter(book_title__icontains=book_or_author)

       
    # the context passes every info from this view to the template
    context = {
        'books':books
    }
    return render(request, 'catalog/index.html', context)

def detail(request, pk):
    book = get_object_or_404(Bookstore, pk=pk)

    context = {
        'book':book
    }
    return render(request, 'catalog/detail.html', context)

def add_to_cart(request, pk):
    item = get_object_or_404(Bookstore, pk=pk)
    user=request.user
    item_query_set = Cart.objects.filter(item=item, user=user, ordered=False)
    if item_query_set.exists():
        item_query_set.quantity +=1
    else:
        order_item, created = Cart.objects.get_or_create(item=item, user=user, ordered=False)
        




    return render(request, 'catalog/detail.html')