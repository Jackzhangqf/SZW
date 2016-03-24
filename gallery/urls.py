# -*-  coding: utf-8  -*-

from django.conf.urls  import include,url,patterns
from gallery.models  import  *
from gallery.views  import  ItemView,PhtotoDetailView,ItemsView,ItemDetailView
from django.conf   import   settings

urlpatterns = patterns('',
	url(r'index/$', ItemView.as_view(),
		name='index'
		),
	url(r'items/$', ItemsView.as_view(),
		name='item_list'
		),
	url(r'item/(?P<pk>\d+)/$', ItemDetailView.as_view(),
		
		name='item_detail'
		),
	url(r'photos/(?P<pk>\d+)/$', PhtotoDetailView.as_view(),
		
		name='photo_detail'
		),
	)

