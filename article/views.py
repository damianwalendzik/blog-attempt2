from django.shortcuts import render
from .models import Article, Comment
def index(request):
    return render(request,'index.html', {})


def articleList(request):
    qs = Article.objects.all()
    data={}
    data['queryset']=qs    
    return render(request,'article/article_list.html', data)

def articleDetailView(request, article_id):
    article_data = Article.objects.get(id=article_id)
    comment_data = Comment.objects.filter(article=article_id)
    data = {
        'queryset': article_data,
        'comments':comment_data
    }
    return render(request, 'article/article_detail.html',data)