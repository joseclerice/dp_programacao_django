from django.contrib import admin
from .models import Category, Book
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    ...


admin.site.register(Category, CategoryAdmin)


class BookAdmin(admin.ModelAdmin):
    ...


admin.site.register(Book, BookAdmin)
