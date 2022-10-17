from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    img = models.CharField(max_length=1000, default="None")
    title = models.CharField(max_length=100, default="None")
    author = models.CharField(max_length=500, default="None")
    categories = models.CharField(max_length=500, default="None")
    description = models.TextField(max_length=1000, default="None")


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Favorite(models.Model):
    title = models.CharField(max_length=150)
    favbooks = models.ManyToManyField(Book)

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title