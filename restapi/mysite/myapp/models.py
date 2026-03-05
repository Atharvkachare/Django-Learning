from django.db import models

class Book(models.Model):  # Make sure "Book" is capitalized exactly like this
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    # add any other fields you want...

    def __str__(self):
        return self.title