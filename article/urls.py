from django.urls import path
from .views import (articleList, index, articleDetailView, 
    articleCreateView, articleDeleteView, deleteMessage, 
    articleUpdateView, commentUpdateView, commentDeleteView)


urlpatterns = [
        path('', index, name='index'),
        path('article_list/', articleList, name='article-list'),
        path('article_list/<int:article_id>/', articleDetailView, name='article_detail'),
        path('create_article/', articleCreateView, name='create-article'),
        path('delete/<int:article_id>/',articleDeleteView,name='delete-article'),
        path('delete/delete_comment/<int:comment_id>/',commentDeleteView,name='delete-comment'),
        path('delete/delete_message/',deleteMessage, name='delete-message'),
        path('article_list/<int:article_id>/update_article',articleUpdateView, name='update-article'),
        path('update_comment/<int:comment_id>',commentUpdateView, name='update-comment'),
    ]
