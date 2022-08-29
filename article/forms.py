from django import forms
from .models import Article, Comment
class CreateNewArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'text']

class CreateNewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']