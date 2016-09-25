"""blog URL Configuration

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
from django.conf.urls import patterns, include, url
from django.contrib import admin
from books import views
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', views.home, name='home'),
    url(r'^blogtopics/$', views.blogtopics, name='blogtopics'),
    url(r'^resources/$', views.resources, name='resources'),
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^progresstracker/$', views.progresstracker, name='progresstracker'),
    url(r'^(?P<category>[\w-]+)/(?P<slug>[\w-]+)/$', views.pt_detail, name='pt_detail'),
    url(r'^(?P<category>[\w-]+)/(?P<slug>[\w-]+)/edit/$', views.post_edit, name='post_edit'),
]
