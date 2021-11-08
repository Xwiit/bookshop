from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import tree


# Create your models here.

STATUS_CHOICES =(
    ('trending', 'Trending'),
    ('bestselling', 'Bestselling'),
)

class Bookstore(models.Model):
   book_author = models.CharField(max_length=200, blank=False, verbose_name='Author')
   book_title = models.CharField(max_length=200, blank=False, null=False, verbose_name='title')
   book_price = models.FloatField(verbose_name='Price', blank=False, null=False,)
   book_cover = models.URLField(max_length=400, verbose_name='Book Cover')
   book_page = models.IntegerField()
   book_status = models.CharField(choices=STATUS_CHOICES, blank=True, null=True, max_length=200)
   book_description = models.TextField()
   book_pdf = models.URLField(max_length=200)
   listed_on = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return f'{self.book_author}, {self.book_title}'

class Cart(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   item = models.ForeignKey(Bookstore, on_delete=models.CASCADE)
   quantity = models.IntegerField(default=1)
   ordered = models.BooleanField(False)
   


class Order(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   items = models.ManyToManyField(Cart)
   ordered = models.BooleanField(False)
   start_date = models.DateTimeField(auto_now_add=True)
   ordered_date = models.DateTimeField()
  

class BookReview(models.Model):
    book = models.ForeignKey(Bookstore, related_name='review', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(blank=False)
    review = models.TextField(blank=False)
    review_date =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('details', args=[self.pk])
    