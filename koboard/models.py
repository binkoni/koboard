from django.db import models
from django.conf import settings
import django.utils.timezone

class Board(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)

class Article(models.Model):
    prev = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=False, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, blank=False, null=False, on_delete=models.CASCADE)
    ctime = models.DateTimeField(blank=False, null=False, default=timezone.now, editable=False)
    mtime = models.DateTimeField(blank=False, null=False, default=timezone.now, editable=False)
    views = models.IntegerField(blank=False, null=False, default=0, editable=False)
    title = models.CharField(max_length=64, blank=False, null=False)
    content = models.TextField(blank=True, null=False)

class Comment(models.Model):
    prev = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=False, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, blank=False, null=False, on_delete=models.CASCADE)
    ctime = models.DateTimeField(blank=False, null=False, default=timezone.now, editable=False)
    mtime = models.DateTimeField(blank=False, null=False, default=timezone.now, editable=False)
    content = models.TextField(blank=True, null=False)

class File(models.Model):
    article = models.ForeignKey(Article, blank=False, null=False, on_delete=models.CASCADE)
    file = models.FileField()

class Image(models.Model):
    image = models.ImageField()

class FileArticleXref(models.Model):
    file = models.ForeignKey(File, blank=False, null=False, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, blank=False, null=False, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('file', 'article'),)

class ImageArticleXref(models.Model):
    image = models.ForeignKey(Image, blank=False, null=False, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, blank=False, null=False, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('image', 'article'),)

class ImageCommentXref(models.Model):
    image = models.ForeignKey(Image, blank=False, null=False, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, blank=False, null=False, on_delete=models.CASCADE)
    class Meta:
        unique_together = (('image', 'comment'),)
