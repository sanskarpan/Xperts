# articles/admin.py
from django.contrib import admin
from .models import Article

class ArticleInline(admin.TabularInline):
    model = Article
    extra = 1

admin.site.register(Article)
