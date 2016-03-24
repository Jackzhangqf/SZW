# -*-  coding: utf-8  -*-
from django.utils.translation import ugettext as _
from django.shortcuts import render,get_object_or_404,get_list_or_404
#
#render()它的用法类似TemplateResponse
#
#render_to_response() 的用法：
#render_to_response('my_template.html',my_context, context_instance=RequestContext(request))
#
#redirect()
#
#get_object_or_404()
#
#get_list_or_404()
#
from django.template import loader,Context,response,Template
#描述了一个渲染模板的使用方法：
#response.TemplateResponse(request, 'entry_list.html', {'entries': Entry.objects.all()})
from django.http import HttpResponse , HttpResponseRedirect,HttpResponseNotFound,Http404
#上述模块中描述了部分的响应类型，现总结如下：
#（1）HttpResponse
#--------完成正常的响应，用法是：
#HttpResponse(mydata)
# (2)  HttpResponseRedirect
#--------完成重定向的响应，用法是：
#
# (3)  HttpResponsePermanentRedirect
# (4)  HttpResponseBadRequest
# (5)   HttpResponseNotFound
# (6)  HttpResponseForbidden
# (7)  HttpResponseNotAllowed
# (8)  HttpResponseGone
# (9)  HttpResponseServerError

# (10) JsonResponse

# (11)  StreamingHttpResponse 

# (12)   FileResponse 
from django.contrib.auth import authenticate,login,logout
import time
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from  IoT.forms import  *
from  IoT.models  import *
#----------------------------------------------------------generic view
from  django.views.generic.list import  ListView
from  django.views.generic.detail  import  DetailView
from  django.views.generic.edit	   import   UpdateView,DeleteView,CreateView
from  django.views.generic.base import TemplateView,RedirectView
# Create your views here.
none_url = '/IoT/home/'
#UserProfileM
#date:2016/2/19  
class  UserProfileDetailV(DetailView):
	template_name = "userprofile_detail.html"
	queryset = UserProfileM.objects.all()
	def get_context_data(self,**kwargs):
		context  =  super(UserProfileDetailV,self).get_context_data(**kwargs)
		context['user'] = User.objects.get(username=self.request.user)
		return  context
	def get_queryset(self):
		queryset=super(UserProfileDetailV,self).get_queryset()
		user = User.objects.get(username=self.request.user)
		q = queryset.filter(user=user)
		return  q
#date:2016/2/19  
class  UserProfileListV(ListView):
	template_name = "userprofile_list.html"
	model = UserProfileM
	queryset = UserProfileM.objects.all()
	def get(self,request, *args, **kwargs):
		self.object_list = self.get_queryset()
		allow_empty = self.get_allow_empty()
		if  len(self.object_list)==0:
			return HttpResponseRedirect('/IoT/userprofile/create/')
		if not allow_empty:
			# When pagination is enabled and object_list is a queryset,
			# it's better to do a cheap query than to load the unpaginated
			# queryset in memory.
			if (self.get_paginate_by(self.object_list) is not None
				and hasattr(self.object_list, 'exists')):
				is_empty = not self.object_list.exists()
			else:
				is_empty = len(self.object_list) == 0
			if is_empty:
				raise Http404(_("Empty list and '%(class_name)s.allow_empty' is False.")
					% {'class_name': self.__class__.__name__})
		context = self.get_context_data()
		return self.render_to_response(context)

	def get_context_data(self,**kwargs):
		context  =  super(UserProfileListV,self).get_context_data(**kwargs)
		context['user'] = User.objects.get(username=self.request.user)
		return  context

	def get_queryset(self):
		queryset=super(UserProfileListV,self).get_queryset()
		user = User.objects.get(username=self.request.user)
		return queryset.filter(user=user)
class  UserProfileCreateV(CreateView):
	""" This is UserProfileCreateV """
	template_name = 'userprofile_create_form.html'
	model = UserProfileM
	#fields = "__all__"
	form_class  = UserProfileForm
	def get_form_kwargs(self):
        		kwargs = super(UserProfileCreateV, self).get_form_kwargs()
        		kwargs.update({
            		'user':self.request.user
        		})
        		return kwargs

class  UserProfileUpdateV(UpdateView):
	""" This is UserProfileUpdateV """
	template_name = 'userprofile_update_form.html'
	model = UserProfileM
	success_url = '/IoT/userprofile/'
	#fields = "__all__"
	form_class  = UserProfileForm
	def get_form_kwargs(self):
		kwargs = super(UserProfileUpdateV, self).get_form_kwargs()
		kwargs.update({
		'user':self.request.user
		})
		return kwargs
	def get_context_data(self,**kwargs):
		context  =  super(UserProfileUpdateV,self).get_context_data(**kwargs)
		context['user'] = User.objects.get(username=self.request.user)
		return  context
	def get_queryset(self):
		queryset=super(UserProfileUpdateV,self).get_queryset()
		user = User.objects.get(username=self.request.user)
		return  queryset.filter(user=user.id)

class  UserProfileDeleteV(DeleteView):
	""" This is UserProfileDeleteV """
	success_url = "/IoT/userprofile/"
	template_name = "userprofile_delete.html"
	queryset = UserProfileM.objects.all()
	def get_context_data(self,**kwargs):
		context  =  super(UserProfileDeleteV,self).get_context_data(**kwargs)
		context['user'] = User.objects.get(username=self.request.user)
		return  context
	def get_queryset(self):
		queryset=super(UserProfileDeleteV,self).get_queryset()
		user = User.objects.get(username=self.request.user)
		q = queryset.filter(user=user.id)
		return  q
	def get(self, request, *args, **kwargs):
        		return self.delete(request, *args, **kwargs)
#UserAccessM
class  UserAccessDetailV(UserProfileDetailV):
	template_name = "useraccess_detail.html"
	queryset = UserAccessM.objects.all()

class  UserAccessListV(UserProfileListV):
	template_name = "useraccess_list.html"
	model = UserAccessM
	none_url = '/IoT/home/'
	queryset = UserAccessM.objects.all()

class  UserAccessCreateV(CreateView):
	""" This is UserAccessCreateV """

class  UserAccessUpdateV(UpdateView):
	""" This is UserAccessUpdateV """

class  UserAccessDeleteV(DeleteView):
	""" This is UserAccessDeleteV """
#RegionM
class  RDBaseList(ListView):
	def get(self,request, *args, **kwargs):
		self.object_list = self.get_queryset()
		allow_empty = self.get_allow_empty()
		if  len(self.object_list)==0:
			return HttpResponseRedirect(none_url)
		if not allow_empty:
			# When pagination is enabled and object_list is a queryset,
			# it's better to do a cheap query than to load the unpaginated
			# queryset in memory.
			if (self.get_paginate_by(self.object_list) is not None
				and hasattr(self.object_list, 'exists')):
				is_empty = not self.object_list.exists()
			else:
				is_empty = len(self.object_list) == 0
			if is_empty:
				raise Http404(_("Empty list and '%(class_name)s.allow_empty' is False.")
					% {'class_name': self.__class__.__name__})
		context = self.get_context_data()
		return self.render_to_response(context)

	def get_context_data(self,**kwargs):
		context  =  super(RDBaseList,self).get_context_data(**kwargs)
		context['user'] = User.objects.get(username=self.request.user)
		return  context
class  RDBaseDetail(DetailView):
	def get_context_data(self,**kwargs):
		context  =  super(UserProfileDetailV,self).get_context_data(**kwargs)
		context['user'] = User.objects.get(username=self.request.user)
		return  context
class  RegionListV(RDBaseList):
	template_name = "region_list.html"
	model = RegionM
	queryset = RegionM.objects.all()
	def get_queryset(self):
		queryset=super(RegionListV,self).get_queryset()
		user = User.objects.get(username=self.request.user)
		access_queryset = UserAccessM.objects.all()
		user_access = access_queryset .filter(user = user)
		access_region = user_access.filter(region_or_dev_flag=True)
		access_dev = user_access.filter(region_or_dev_flag= False)
		q_list=[]
		for  access_r   in  access_region:
			q_list.append(access_r.region_id)

		for  access_d  in  access_dev:
			q1=DevM.objects.get(dev_id=access_d.dev_id)
			q2=q1.region.region_id
			if  q2  not  in  q_list:
				q_list.append(q2)
		return queryset.filter(region_id__in=q_list)

#class RegionDetailV(DetailView):
#	template_name = "region_detail.html"
#	model = RegionM
#	queryset = RegionM.objects.all()
#	def get_context_data(self,**kwargs):
#		context  =  super(RegionDetailV,self).get_context_data(**kwargs)
#		obj=context.get('object',None)
#		if obj :
#			access_objs = UserAccessM.objects.filter(user=self.request.user)
#			region_access_objs = access_objs.filter(region_or_dev_flag=True)
#			dev_access_objs = access_objs.filter(region_or_dev_flag=False)
#			region_a_obj = region_access_objs.filter(region_id=obj.region_id)
#			if region_a_obj:
#				dev_list = get_list_or_404(DevM,region=obj)
#			else:
#				q_list = []
#				for  dev_a  in  dev_access_objs:
#					#q = DevM.objects.filter(dev_id = dev_a.dev_id)[0]
#					q  =  get_object_or_404(DevM, dev_id = dev_a.dev_id)
#					if q.region.region_id == obj.region_id:
#						q_list.append(q.dev_id)
#				dev_list =  get_list_or_404(DevM,dev_id__in=q_list)
#		context["dev_list"] = dev_list
#		context['user'] = self.request.user
#		return  context

class  RegionDetailV(ListView):
	template_name = "region_detail.html"
	model = DevM
	queryset = DevM.objects.all()
	def get(self, request, *args, **kwargs):
		self.object_list = self.get_queryset(**kwargs)
		allow_empty = self.get_allow_empty()

		if not allow_empty:
			# When pagination is enabled and object_list is a queryset,
			# it's better to do a cheap query than to load the unpaginated
			# queryset in memory.
			if (self.get_paginate_by(self.object_list) is not None
				and hasattr(self.object_list, 'exists')):
				is_empty = not self.object_list.exists()
			else:
				is_empty = len(self.object_list) == 0
			if is_empty:
				raise Http404(_("Empty list and '%(class_name)s.allow_empty' is False.")
				% {'class_name': self.__class__.__name__})
		context = self.get_context_data(**kwargs)
		return self.render_to_response(context)
	def  get_queryset(self,**kwargs):
		queryset=super(RegionDetailV,self).get_queryset()
		obj_pk=kwargs.get('region_pk',None)
		q_list = []
		if  obj_pk :
			obj = get_object_or_404(RegionM,id=obj_pk)
			#obj = RegionM.objects.get(pk=obj_pk)
			#print type(obj_pk)
		else:
			raise Http404(_('obj_Invalid page Not accessprofile!'))
		if obj :
			access_objs = UserAccessM.objects.filter(user=self.request.user)
			region_access_objs = access_objs.filter(region_or_dev_flag=True)
			dev_access_objs = access_objs.filter(region_or_dev_flag=False)
			region_a_obj = region_access_objs.filter(region_id=obj.region_id)
			if region_a_obj:
				dev_list = get_list_or_404(DevM,region=obj)
				#print len(dev_list)
				for  dev_l   in  dev_list:
					q_list.append(dev_l.dev_id)
			else:			
				for  dev_a  in  dev_access_objs:
					#q = DevM.objects.filter(dev_id = dev_a.dev_id)[0]
					q  =  get_object_or_404(DevM, dev_id = dev_a.dev_id)
					if q.region.region_id == obj.region_id:
						q_list.append(q.dev_id)
				#queryset =  get_list_or_404(DevM,dev_id__in=q_list)
		else:
			raise Http404(_('List_Invalid page Not accessprofile!'))
		print  q_list
		return  queryset.filter(dev_id__in=q_list) 
	def  get_context_data(self,**kwargs):
		context  =  super(RegionDetailV,self).get_context_data(**kwargs)
		context['user'] = self.request.user
		obj_pk=kwargs.get('region_pk', None)
		print obj_pk
		if  obj_pk:
			obj = get_object_or_404(RegionM,id=obj_pk)
		else:
			raise Http404(_('Invalid page Not accessprofile!'))
		context['object'] = obj
		return  context


#DevM
class DevListV(RDBaseList):
	template_name = "dev_list.html"
	model = DevM
	queryset = DevM.objects.all()
	def get_queryset(self):
		queryset=super(DevListV,self).get_queryset()
		user = User.objects.get(username=self.request.user)
		access_queryset = UserAccessM.objects.all()
		user_access = access_queryset .filter(user = user)
		access_region = user_access.filter(region_or_dev_flag=True)
		access_dev = user_access.filter(region_or_dev_flag= False)
		q_list=[]
		for  access_r  in  access_region:
			try:
				q1=RegionM.objects.get(region_id = access_r.region_id)
				q2=DevM.objects.filter(region=q1)
			except:
				print  "[DevListV]:Create a error!"
			if len(q2)   != 0:
				for temp  in  q2:
					q_list.append(temp.dev_id)
		for  access_d  in  access_dev:
			if  access_d  not  in   q_list:
				q_list.append(access_d.dev_id)
		return queryset.filter(dev_id__in=q_list)
"""
class  DevDetailV(DetailView):
	template_name = "dev_detail.html"
	model = DevM
	queryset = DevM.objects.all()
	def  get_context_data(self,**kwargs):
		context  =  super(DevDetailV,self).get_context_data(**kwargs)
		obj=context.get('object',None)
		if  obj:
			dev_region_id = obj.region.region_id
			dev_id  =  obj.dev_id
			access_objs = UserAccessM.objects.filter(user=self.request.user)
			region_access_objs = access_objs.filter(region_or_dev_flag=True)
			dev_access_objs = access_objs.filter(region_or_dev_flag=False)
			r_access = region_access_objs.filter(region_id=dev_region_id)
			if  r_access:
				sensor_list = SensorM.objects.filter(dev=obj)
			else:
				d_access = dev_access_objs.filter(dev_id=dev_id)
				if d_access:
					sensor_list = SensorM.objects.filter(dev=obj)
				else:
					raise Http404(_('Invalid page Not accessprofile!'))
			context["sensor_list"] = sensor_list
			context["user"] = self.request.user
		return context
"""				

class  DevDetailV(ListView):
	template_name = "dev_detail.html"
	model = SensorM
	queryset = SensorM.objects.all()
	def get(self, request, *args, **kwargs):
		self.object_list = self.get_queryset(**kwargs)
		allow_empty = self.get_allow_empty()

		if not allow_empty:
			# When pagination is enabled and object_list is a queryset,
			# it's better to do a cheap query than to load the unpaginated
			# queryset in memory.
			if (self.get_paginate_by(self.object_list) is not None
				and hasattr(self.object_list, 'exists')):
				is_empty = not self.object_list.exists()
			else:
				is_empty = len(self.object_list) == 0
			if is_empty:
				raise Http404(_("Empty list and '%(class_name)s.allow_empty' is False.")
				% {'class_name': self.__class__.__name__})
		context = self.get_context_data(**kwargs)
		return self.render_to_response(context)

	def  get_context_data(self,**kwargs):
		context  =  super(DevDetailV,self).get_context_data(**kwargs)
		context['user'] = self.request.user
		obj_pk=kwargs.get('dev_pk', None)
		print obj_pk
		if  obj_pk:
			obj = get_object_or_404(DevM,id=obj_pk)
		else:
			raise Http404(_('Invalid page Not accessprofile!'))
		context['object'] = obj
		return  context

	def get_queryset(self,**kwargs):
		queryset = super(DevDetailV,self).get_queryset()
		obj_pk=kwargs.get('dev_pk',None)
		q_list = []
		if  obj_pk :
			obj = get_object_or_404(DevM,id=obj_pk)
			#obj = RegionM.objects.get(pk=obj_pk)
			#print type(obj_pk)
		else:
			raise Http404(_('obj_Invalid page Not accessprofile!'))
		dev_region_id = obj.region.region_id
		dev_id  =  obj.dev_id
		access_objs = UserAccessM.objects.filter(user=self.request.user)
		region_access_objs = access_objs.filter(region_or_dev_flag=True)
		dev_access_objs = access_objs.filter(region_or_dev_flag=False)
		r_access = region_access_objs.filter(region_id=dev_region_id)
		if  r_access:
			sensor_list = SensorM.objects.filter(dev=obj)
			for  sensor_l  in  sensor_list:
				q_list.append(sensor_l.id)
		else:
			d_access = dev_access_objs.filter(dev_id=dev_id)
			if d_access:
				sensor_list = SensorM.objects.filter(dev=obj)
				for  sensor_l  in  sensor_list:
					q_list.append(sensor_l.id)
			else:
				raise Http404(_('Invalid page Not accessprofile!'))
		#context["sensor_list"] = sensor_list
		#context["user"] = self.request.user
		return queryset.filter(id__in=q_list)




#SensorM
class SensorListV(RDBaseList):
	template_name = "sensor_list.html"
	model = SensorM
	queryset = SensorM.objects.all()
	def  get_queryset(self):
		queryset=super(SensorListV,self).get_queryset()
		#get the user's dev_list----------start
		q_dev=get_list_or_404(DevM.objects.all())
		user = User.objects.get(username=self.request.user)
		access_queryset = UserAccessM.objects.all()
		user_access = access_queryset .filter(user = user)
		access_region = user_access.filter(region_or_dev_flag=True)
		access_dev = user_access.filter(region_or_dev_flag= False)
		q_list=[]
		for  access_r  in  access_region:
			try:
				q1=RegionM.objects.get(region_id = access_r.region_id)
				q2=DevM.objects.filter(region=q1)
			except:
				print  "[DevListV]:Create a error!"
			if len(q2)   != 0:
				for temp  in  q2:
					q_list.append(temp.dev_id)
		for  access_d  in  access_dev:
			if  access_d  not  in   q_list:
				q_list.append(access_d.dev_id)
		#get the user's dev_list-------------end 
		qqq_list=[]
		for  dev_id_temp  in q_list:
			object = get_object_or_404(DevM,dev_id = dev_id_temp)
			qq1=SensorM.objects.filter(dev=object)
			#if  len(qq1) == 0:
				#raise Http404(_('1111Invalid page Not accessprofile!'))
			for q  in  qq1 :
				qqq_list.append(q.id)

		return  queryset.filter(id__in=qqq_list)
"""
class  SensorDetailV(DetailView):
	template_name = "sensor_detail.html"
	model = SensorM
	queryset = SensorM.objects.all()
	def  get_context_data(self,**kwargs):
		context  =  super(SensorDetailV,self).get_context_data(**kwargs)
		obj=context.get('object',None)
		if  obj:
			dev = obj.dev
			dev_region_id = dev.region.region_id
			dev_id  =  obj.dev.dev_id
			#raise Http404(_('Invalid page Not accessprofile!'))
			access_objs = UserAccessM.objects.filter(user=self.request.user)
			region_access_objs = access_objs.filter(region_or_dev_flag=True)
			dev_access_objs = access_objs.filter(region_or_dev_flag=False)
			try:
				r_access = region_access_objs.get(region_id=dev_region_id)
			except r_access.model.DoesNotExist:
				try:
					d_access = dev_access_objs.get(dev_id=dev_id)
				except  d_access.model.DoesNotExist:
					raise Http404(_('Invalid page Not accessprofile!'))
			data_list = DataM.objects.filter(sensor=obj)
			context["data_list"] = data_list[0:6]
			context["user"] = self.request.user
			return context
"""
class  SensorDetailV(ListView):
	template_name = "sensor_detail.html"
	model = DataM
	queryset = DataM.objects.all()
	def get(self, request, *args, **kwargs):
		self.object_list = self.get_queryset(**kwargs)
		allow_empty = self.get_allow_empty()

		if not allow_empty:
			# When pagination is enabled and object_list is a queryset,
			# it's better to do a cheap query than to load the unpaginated
			# queryset in memory.
			if (self.get_paginate_by(self.object_list) is not None
				and hasattr(self.object_list, 'exists')):
				is_empty = not self.object_list.exists()
			else:
				is_empty = len(self.object_list) == 0
			if is_empty:
				raise Http404(_("Empty list and '%(class_name)s.allow_empty' is False.")
				% {'class_name': self.__class__.__name__})
		context = self.get_context_data(**kwargs)
		return self.render_to_response(context)

	def  get_context_data(self,**kwargs):
		context  =  super(SensorDetailV,self).get_context_data(**kwargs)
		context['user'] = self.request.user
		obj_pk=kwargs.get('sensor_pk', None)
		#print obj_pk
		if  obj_pk:
			obj = get_object_or_404(SensorM,id=obj_pk)
		else:
			raise Http404(_('Invalid page Not accessprofile!'))
		context['object'] = obj
		return  context
	def  get_queryset(self,**kwargs):
		queryset =  super(SensorDetailV,self).get_queryset()
		obj_pk=kwargs.get('sensor_pk',None)
		q_list = []
		if  obj_pk :
			obj = get_object_or_404(SensorM,id=obj_pk)
			#obj = RegionM.objects.get(pk=obj_pk)
			#print type(obj_pk)
		else:
			raise Http404(_('obj_Invalid page Not accessprofile!'))
		dev = obj.dev
		dev_region_id = dev.region.region_id
		dev_id  =  obj.dev.dev_id
		#raise Http404(_('Invalid page Not accessprofile!'))
		access_objs = UserAccessM.objects.filter(user=self.request.user)
		region_access_objs = access_objs.filter(region_or_dev_flag=True)
		dev_access_objs = access_objs.filter(region_or_dev_flag=False)
		r_access = region_access_objs.filter(region_id=dev_region_id)
		if  r_access:
			data_list = DataM.objects.filter(sensor=obj)
			for  data_l  in  data_list:
				q_list.append(data_l.id)
		else:
			d_access = dev_access_objs.get(dev_id=dev_id)
			if d_access:
				data_list = DataM.objects.filter(sensor=obj)
				for  data_l  in  data_list:
					q_list.append(data_l.id)	
			else:
				raise Http404(_('Invalid page Not accessprofile!'))
		
		#context["data_list"] = data_list[0:6]
		#context["user"] = self.request.user
		return queryset.filter(id__in=q_list)
#DataM
#SensorThresholdM
class SensorThresholdListV(ListView):
	template_name = "sensorthreshold_list.html"
	model = SensorThresholdM
	def   get_queryset(self):
		queryset= super(SensorThresholdListV,self).get_queryset()
		return queryset.filter(user=self.request.user)
	def   get_context_data(self,**kwargs):
		context  =  super(SensorThresholdListV,self).get_context_data(**kwargs)
		context['user'] =self.request.user
		return  context
class  SensorThresholdCreateV(CreateView):
	""" SensorThresholdCreateV """
	template_name = 'sensorthreshold_create_form.html'
	model = SensorThresholdM
	success_url =  "/IoT/sensorthreshold/"
	#fields = "__all__"
	form_class  = SensorThresholdForm
	def get_form_kwargs(self):
        		kwargs = super(SensorThresholdCreateV, self).get_form_kwargs()
        		kwargs['initial'] ={'sensor_id':self.kwargs.get('sensor_id')}
        		kwargs.update({
            		'user':self.request.user
        		})
        		return kwargs
class  SensorThresholdDeleteV(DeleteView):
	""" SensorThresholdDeleteV """
	success_url = "/IoT/sensorthreshold/"
	template_name = "sensorthreshold_delete.html"
	queryset = SensorThresholdM.objects.all()
	def get_context_data(self,**kwargs):
		context  =  super(SensorThresholdDeleteV,self).get_context_data(**kwargs)
		context['user'] =self.request.user
		return  context
	def get_queryset(self):
		queryset=super(SensorThresholdDeleteV,self).get_queryset()
		q = queryset.filter(user=self.request.user)
		return  q
	def get(self, request, *args, **kwargs):
        		return self.delete(request, *args, **kwargs)
class  SensorThresholdUpdateV(UpdateView):
	template_name = 'sensorthreshold_update_form.html'
	model = SensorThresholdM
	success_url =  "/IoT/sensorthreshold/"
	form_class  = SensorThresholdForm
	def get_form_kwargs(self):
		kwargs = super(SensorThresholdUpdateV, self).get_form_kwargs()
		kwargs['initial'] ={'sensor_id':self.object.sensor_id}
		kwargs.update({
		'user':self.request.user
		})
		return kwargs
	def get_context_data(self,**kwargs):
		context  =  super(SensorThresholdUpdateV,self).get_context_data(**kwargs)
		context['user'] = User.objects.get(username=self.request.user)
		return  context
	def get_queryset(self):
		queryset=super(SensorThresholdUpdateV,self).get_queryset()
		return queryset.filter(user=self.request.user)
#UserDevM


#/IoT/userlogin
def  UserLoginV(request):
	curtime = time.strftime("%Y-%m-%d  %H:%M:%S",time.localtime())

	if request.method == 'POST':
		print("POST")
		username = request.POST['name']
		password = request.POST['password']
		user = authenticate(username = username,password=password)
		if user and  user.is_active:
			login(request, user)
			print "Come in!"
			return HttpResponseRedirect('/IoT/home/')
	if request.method == 'GET':
		print "This is a GET !"
	return response.TemplateResponse(request,'login_z.html',{})
#/IoT/userlogout
def UserLogoutV(request):
	logout(request)
	return HttpResponseRedirect('/IoT/userlogin/')
from blog.models import UserForm
#/IoT/accounts/
@login_required(login_url='/IoT/userlogin/')
def UserHomeV(request):
	query_user = User.objects.get(username=request.user)
	test_form = TestForm()
	#query_user.last_name = u'中文'
	return response.TemplateResponse(request,'base_z.html',{"user":query_user})
