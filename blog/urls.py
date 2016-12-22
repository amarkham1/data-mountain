from django.conf.urls import url, include
from django.contrib import admin
import django.contrib.auth.views
from books import views
admin.autodiscover()
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', django.contrib.auth.views.login, name='login'),
    url(r'^account/logout$', django.contrib.auth.views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^home/$', views.home, name='home'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^blogtopics/computer-science/$', views.compsci, name='computer-science'),
    url(r'^blogtopics/data-science/$', views.datasci, name='data-science'),
    url(r'^blogtopics/other/$', views.other, name='other'),
    url(r'^blogtopics/$', views.blogtopics, name='blogtopics'),
    url(r'^resources/$', views.resources, name='resources'),
    url(r'^resources/edit/$', views.resources_post_edit, name='resources_post_edit'),
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^progresstracker/$', views.progresstracker, name='progresstracker'),
    url(r'^blogtopics/(?P<category>[\w-]+)/(?P<slug>[\w-]+)/$', views.bt_detail, name='bt_detail'),
    url(r'^(?P<category>[\w-]+)/(?P<slug>[\w-]+)/$', views.pt_detail, name='pt_detail'),
    url(r'^blogtopics/(?P<category>[\w-]+)/(?P<slug>[\w-]+)/edit/$', views.post_edit, name='bt_post_edit'),
    url(r'^(?P<category>[\w-]+)/(?P<slug>[\w-]+)/edit/$', views.post_edit, name='pt_post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^blogtopics/(?P<category>[\w-]+)/(?P<slug>[\w-]+)/remove/$', views.post_remove, name='bt_post_remove'),
    url(r'^(?P<category>[\w-]+)/(?P<slug>[\w-]+)/remove/$', views.post_remove, name='pt_post_remove'),
    url(r'^blogtopics/(?P<category>[\w-]+)/(?P<slug>[\w-]+)/publish/$', views.post_publish, name='bt_post_publish'),
    url(r'^(?P<category>[\w-]+)/(?P<slug>[\w-]+)/publish/$', views.post_publish, name='pt_post_publish'),
]
