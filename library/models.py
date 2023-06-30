from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category (models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Book (models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=164)
    slug = models.SlugField()
    pages = models.IntegerField(max_length=5)
    author = models.TextField(max_length=50)
    published_in = models.DateField()
    synopsis = models.TextField(max_length=1000)
    synopsis_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
        default=None
    )
    author_pub = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

# Create your models here.
