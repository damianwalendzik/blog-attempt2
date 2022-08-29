from django.urls import path
from .views import articleList, index
urlpatterns = [
        path('', index, name='index'),
        path('article_list', articleList, name='article-list'),
    ]