from django.contrib import admin
from .models import Board, Article, File, Image, Comment
admin.site.register((Board, Article, File, Image, Comment))
