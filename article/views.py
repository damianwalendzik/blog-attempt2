from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import (
    CreateNewArticle, CreateNewComment, DeleteArticle, 
    DeleteComment, UpdateArticle, UpdateComment)
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer, CommentSerializer
def index(request):
    return render(request,'index.html', {})



def articleList(request):
    qs = Article.objects.all()
    data={}
    data['queryset']=qs    
    return render(request,'article/article_list.html', data)

def articleDetailView(request, article_id):
    id=article_id
    data = {}
    article_data = Article.objects.get(id=id)
    comment_data = Comment.objects.filter(article=id)
    data['queryset'] = article_data
    data['comments'] = comment_data
    data['form'] = 0
    if request.POST:
        form = CreateNewComment(request.POST)
        if form.is_valid():
            new_text = form.cleaned_data["text"]
            new_comment = Comment(article_id=article_id, user=request.user, text=new_text)
            new_comment.save()
            data['form'] = form
        else:
            form = CreateNewComment()
            data['form'] = form
            
    return render(request, 'article/article_detail.html',data)

def articleCreateView(request):
    if request.POST:
        form = CreateNewArticle(request.POST)
        if form.is_valid():
            new_title = form.cleaned_data["title"]
            new_text = form.cleaned_data["text"]
            new_author= form.cleaned_data["author"]
            new_blog = Article(title=new_title, author=new_author, text=new_text)
            #new_blog.author = request.author
            new_blog.save()
    else:
        form = CreateNewArticle()
    return render(request, 'article/create_article.html',{'form':form})

def articleDeleteView(request, article_id):
    article = Article(id=article_id)
    if request.POST:
        form = DeleteArticle(request.POST)
        if form.is_valid():
            article.delete()
    else:
        form = DeleteArticle()
    print(form)
    return render(request, 'article/article_delete.html',{'form':form})

def deleteMessage(request):
    return render(request,'article/delete_message.html', {})

def articleUpdateView(request, article_id):
    if request.POST:
        form = UpdateArticle(request.POST)
        if form.is_valid():
            new_text = form.cleaned_data["text"]
            Article.objects.filter(id=article_id).update(text=new_text)
    else:
        form = UpdateArticle()
    print(form)
    return render(request, 'article/article_update.html',{'form':form})

def commentUpdateView(request, comment_id, *args, **kwargs):
    if request.POST:
        form = UpdateComment(request.POST)
        if form.is_valid():
            new_text = form.cleaned_data["text"]
            Comment.objects.filter(id=comment_id).update(text=new_text)
    else:
        form = UpdateComment()
    print(form)
    return render(request, 'article/comment_update.html',{'form':form})

def commentDeleteView(request, comment_id):
    comment = Comment(id=comment_id)
    if request.POST:
        form = DeleteComment(request.POST)
        if form.is_valid():
            comment.delete()
    else:
        form = DeleteComment()
    print(form)
    return render(request, 'article/comment_delete.html',{'form':form})

def deleteMessage(request):
    return render(request,'article/delete_message.html', {})
