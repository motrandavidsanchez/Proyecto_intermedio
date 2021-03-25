from django.contrib import admin
from django.urls import path, include

from webempresa import settings
from webempresa.router import router

urlpatterns = [

    path('', include('core.urls')),
    path('service/', include('service.urls')),
    path('blog/', include('blog.urls')),
    path('page/', include('page.urls')),
    path('contact/', include('contact.urls')),

    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
