from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^',include('shop.urls')),
    path('admin/', admin.site.urls), 
    url(r'shop/',include('shop.urls')),
    url(r'blog/',include('blog.urls'))


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
