from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('core.urls')),
    path('api/', include('core.urls')),
    path('api/expertise/', include('industry.urls')),
    path('api/tools/', include('tools.urls')),
    path('api/', include('workex.urls')),
    path('api/', include('events.urls')),  # Include the events app URLs
    path('api/webadmin/', include('webadmin.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
    path('api/', include('blogs.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api-auth/', include('rest_framework.urls')),  # for browsable API login
    path('auth/', include('core.urls')),  # Include the core app URLs
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('api/', include('cohorts.urls')),
    path('navigation/', include('navigation.urls')),
    path('', RedirectView.as_view(url='/admin/', permanent=False)),  # Redirect root to /api/

    
    


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)