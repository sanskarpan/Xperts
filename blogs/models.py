from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = RichTextUploadingField()
    thumbnail = models.ImageField(upload_to='blog_thumbnails/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # SEO and OG fields
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    og_title = models.CharField(max_length=255, blank=True, null=True)
    og_description = models.TextField(blank=True, null=True)
    og_image = models.ImageField(upload_to='og_images/', blank=True, null=True)

    # Keyword tags
    tags = TaggableManager()

    def __str__(self):
        return self.title
