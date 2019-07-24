from django.contrib import admin
from .models import *
admin.site.register((Board, Article, File, Image, Comment, ImageArticleXref, ImageCommentXref))
