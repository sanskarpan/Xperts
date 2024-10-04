# blogs/urls.py
from django.urls import path
from .views import BlogPostListCreateView, BlogPostDetailView

urlpatterns = [
    path('blogs/', BlogPostListCreateView.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', BlogPostDetailView.as_view(), name='blog-detail'),
]
