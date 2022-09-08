
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

class DeleteArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = []

class DeleteComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = []

class UpdateArticle(forms.ModelForm):
    class Meta: 
        model = Article
        fields = ['text']

class UpdateComment(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['text']