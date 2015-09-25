from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.do_login, name='login'),
    url(r'^logout/$', views.do_logout, name='logout'),
]