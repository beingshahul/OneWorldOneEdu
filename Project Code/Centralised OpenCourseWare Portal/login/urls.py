from django.conf.urls import patterns, include, url
from login import views


urlpatterns =patterns('',

    url(r'^$', views.login_view, name='login'),
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^logout/$', views.logout_view, name='logout')
       
)