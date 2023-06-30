from django.shortcuts import render
from library.models import Book


def home(request):
    library = Book.objects.filter(
        is_published=True,
    ).order_by('-id')
    return render(request, "library/pages/home.html", context={
        'library': library,
    })
