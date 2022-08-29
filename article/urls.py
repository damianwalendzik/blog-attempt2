from django.urls import path
from .views import articleList, index, articleDetailView, articleCreateView, articleDeleteView


urlpatterns = [
        path('', index, name='index'),
        path('article_list/', articleList, name='article-list'),
        path('article_list/<int:article_id>/', articleDetailView, name='article_detail'),
        path('create_article/', articleCreateView, name='create-article'),
        path('article_list/delete/<int:article_id>',articleDeleteView,name='delete-article'),
    ]
