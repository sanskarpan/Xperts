from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    search_fields = ('title', 'author__username')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'content', 'thumbnail', 'tags')
        }),
        ('SEO Fields', {
            'fields': ('meta_title', 'meta_description')
        }),
        ('Open Graph Fields', {
            'fields': ('og_title', 'og_description', 'og_image')
        }),
    )
