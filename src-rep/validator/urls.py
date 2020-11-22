from django.contrib import admin
from django.urls import path
from blog.views import home, ip, mac
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('ip/', ip, name='ip'),
    path('mac/', mac, name='mac'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
