"""checkdone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, patterns
from django.contrib import admin
from todos import views
from django.views.static import *
from django.conf.urls.static import static
from django.conf.urls import (
handler400, handler403, handler404, handler500
)

'''urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^search/form', views.search_form),
    url(r'^search/', views.search),
    url(r'^todo/', views.show_all),
    url(r'^add/', views.add_new),
    url(r'^delete/(?P<id>\d+)/$', views.delete_id),
    url(r'^check/(?P<id>\d+)/$', views.check_id),
    #url(r'^.*', views.no_page),
]'''
urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^search/form', views.search_form),
    url(r'^search/', views.search),
    url(r'^todo/', views.show_all),
    url(r'^add/', views.add_new),
    url(r'^delete/(?P<id>\d+)/$', views.delete_id),
    url(r'^check/(?P<id>\d+)/$', views.check_id),
    #url(r'^(.*)', views.no_page),
)

#handler404 = 'views.no_page'
#handler404 = views.no_page()

#handler404 = 'views.http_error'
#handler500 = 'views.http_error'

#handler404 = views.http_error()
#handler500 = views.http_error()
