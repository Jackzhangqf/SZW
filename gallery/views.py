# -*-  coding: utf-8  -*-
from django.shortcuts import render

# Create your views here.
from  django.views.generic.list import  ListView
from  django.views.generic.detail  import  DetailView
from  django.views.generic.base import TemplateView

from  gallery.models  import  Item,Photo

class  ItemView(TemplateView):
	template_name = "index.html"
	def  get_context_data(self,**kwargs):
		context = super(ItemView,self).get_context_data(**kwargs)
		context["item_list"] = Item.objects.all()
		return context

class  ItemsView(ListView):
	template_name = "items_list.html"
	#model = Item
	queryset = Item.objects.all()
	allow_empty = True

class  ItemDetailView(DetailView):
	template_name = "items_detail.html"
	#model = Item
	queryset = Item.objects.all()
	

class  PhtotoDetailView(DetailView):
	template_name = "photos_detail.html"
	#model = Photo
	queryset = Photo.objects.all()
	