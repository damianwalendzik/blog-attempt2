from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    text = models.CharField(max_length=5000)
    date = datetime.now()
    def __str__(self):
        return self.title
class Comment(models.Model):
    blog = models.ForeignKey(Article, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000, blank=False)
    date=datetime.now()
    def __str__(self):
        return self.text