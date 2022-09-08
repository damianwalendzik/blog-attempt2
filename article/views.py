from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import CreateNewArticle, CreateNewComment, DeleteArticle
from django.shortcuts import get_object_or_404
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
