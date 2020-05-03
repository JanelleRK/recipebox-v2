from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Recipes(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField(max_length=140)
    time_req = models.CharField(max_length=25)
    instructions = models.TextField()

    def __str__(self):
        return self.title
