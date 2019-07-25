from django import forms
from .models import *

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
