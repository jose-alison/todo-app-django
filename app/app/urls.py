from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

def statics_urls():
    if settings.DEBUG:
        return static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    else:
        return static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
] + statics_urls()
