"""myadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mongo.views import *
from django.contrib.staticfiles.urls import static
from . import settings
admin.autodiscover()
# from mongoadmin import site
urlpatterns = [
    # url(r'^admin/', include(site.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^product/$', index),
    url(r'^productdel/$', del_classes),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_URL }),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)