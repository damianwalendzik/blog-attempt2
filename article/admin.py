from django.contrib import admin
from .models import Article, Comment
admin.site.register(Article)
admin.site.register(Comment)


# Register your models here.
class BlogInstanceInline(admin.TabularInline):
    model = Article

class CommentInstanceInline(admin.TabularInline):
    model = Comment


class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogInstanceInline]