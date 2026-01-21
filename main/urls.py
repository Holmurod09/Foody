from django.contrib import admin
from django.urls import path, include
from models.views import home
from django.conf import settings
from django.conf.urls.static import static

handler404 = "models.views.custom_404"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)