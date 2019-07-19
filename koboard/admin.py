from django.contrib import admin
from .models import Board, Article
admin.site.register((Board, Article))
