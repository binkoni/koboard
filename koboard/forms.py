from django import forms
from .models import *

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('user',)
        widgets = {'prev': forms.HiddenInput()}

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('user',)
        widgets = {
            'prev': forms.HiddenInput(),
            'article': forms.HiddenInput()
        }

class FileModelForm(forms.ModelForm):
    class Meta:
        model = File

class ImageModelForm(forms.ModelForm):
    class Meta:
        model = Image
