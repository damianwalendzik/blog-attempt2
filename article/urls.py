from django.urls import path
from .views import articleList, index, articleDetailView
urlpatterns = [
        path('', index, name='index'),
        path('article_list/', articleList, name='article-list'),
        path('article_list/<int:article_id>/', articleDetailView, name='article_detail')
    ]