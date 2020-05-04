from django.contrib import admin
from .models import Book,Genre,Usedbook,Newbook,Wishlist

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Usedbook)
admin.site.register(Newbook)
admin.site.register(Wishlist)