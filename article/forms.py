from django import forms
from .models import Article
class CreateNewArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'text']