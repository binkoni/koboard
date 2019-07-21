from django.db import models
from django.conf import settings

class Board(models.Model):
    name = models.TextField(null=False, blank=False)

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=False, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, blank=False, null=False, on_delete=models.CASCADE)
    title = models.TextField(null=False, blank=False)
    content = models.TextField(null=True, blank=True)

class File(models.Model):
    article = models.ForeignKey(Article, blank=False, null=False, on_delete=models.CASCADE)
    file = models.FileField()

class Image(models.Model):
    article = models.ForeignKey(Article, blank=False, null=False, on_delete=models.CASCADE)
    image = models.ImageField()

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=False, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, blank=False, null=False, on_delete=models.CASCADE)
