from django.contrib import admin
from django.urls import path
from blog.views import home, ip, mac
from django.conf import settings
from django.conf.urls.static import static

from testform.views import iphome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('ip/', ip, name='ip'),
    path('mac/', mac, name='mac'),

    path('iphome/', iphome, name='iphome'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
