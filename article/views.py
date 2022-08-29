from django.shortcuts import render
from .models import Article, Comment
def index(request):
    return render(request,'index.html', {})


def articleList(request):
    qs = Article.objects.all()
    data = {
        'queryset':qs
    }      
    return render(request,'article/article_list.html', data)