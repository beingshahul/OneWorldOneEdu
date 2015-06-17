from django.conf.urls import patterns, include, url
from search import views


urlpatterns =patterns('',
	url(r'^$', views.search, name='search'),
    url(r'^provider/$', views.sprovider, name='provider'),
    url(r'^provider/(?P<arg>.+)/$', views.sprovider, name='sprovider'),
    url(r'^language/$', views.slanguage, name='language'),
    url(r'^language/(?P<arg>[\w-]+)/$', views.slanguage, name='slanguage'),
    url(r'^category/$', views.scategory, name='category'),
    url(r'^category/(?P<arg>[\w-]+)', views.scategory, name='scategory'),
    url(r'^details/(?P<slug>[\w-]+)', views.detail_view, name='course_details'),
       
)