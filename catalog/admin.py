from django.contrib import admin
from . models import BookReview, Bookstore, Cart, Order
# Register your models here.

admin.site.register(Bookstore)
admin.site.register(BookReview)
admin.site.register(Cart)
admin.site.register(Order)