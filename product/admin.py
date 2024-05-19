from django.contrib import admin

from product.cloth.models import Cloth, Style
from product.book.models import Author, Category, Book, Publisher
from product.mobile.models import Mobile, Type

# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Style)
admin.site.register(Cloth)
admin.site.register(Type)
admin.site.register(Mobile)