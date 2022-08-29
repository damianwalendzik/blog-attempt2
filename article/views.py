from django.shortcuts import render
from .models import Article, Comment
from .forms import CreateNewArticle
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

def articleCreateView(request):
    if request.POST:
        form = CreateNewArticle(request.POST)
        print(form)
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