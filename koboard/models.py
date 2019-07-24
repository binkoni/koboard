from django.db import models
from django.conf import settings

class Board(models.Model):
    name = models.TextField(null=False, blank=False)

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=False, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, blank=False, null=False, on_delete=models.CASCADE)
    title = models.TextField(null=False, blank=False)
    content = models.TextField(null=False, blank=True)

class File(models.Model):
    article = models.ForeignKey(Article, blank=False, null=False, on_delete=models.CASCADE)
    file = models.FileField()

class Image(models.Model):
    image = models.ImageField()

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=False, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, blank=False, null=False, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=True)

class ImageArticleXref(models.Model):
    models.ForeignKey(Image, blank=False, null=False, on_delete=models.CASCADE)
    models.ForeignKey(Article, blank=False, null=False, on_delete=models.CASCADE)


class ImageCommentXref(models.Model):
    models.ForeignKey(Image, blank=False, null=False, on_delete=models.CASCADE)
    models.ForeignKey(Comment, blank=False, null=False, on_delete=models.CASCADE)
