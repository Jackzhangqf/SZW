# -*-  coding: utf-8   -*-
from django.utils import timezone
from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
#下面是在定义域时的一些选项Field options:
#null   如果为True，将会把该域数据存储为NULL
#blank    默认为真，该域允许为空
#choices
#db_column
#db_index
#db_tablespace
#default
#editable
#error_messages
#help_text
#primary_key
#unique
#unique_for_date
#unique_for_month
#unique_for_year
#verbose_name
#validators
#下面是数据库下面定义的模型域类型Field types：
#AutoField
#BigIntegerField
#BinaryField
#BooleanField      用来描述布尔类型的值的
#CharField
#CommaSeparatedIntegerField
#DateField
#DateTimeField
#DecimalField
#DurationField
#EmailField
#FileField
#FilePathField
#FloatField
#ImageField
#IntegerField
#GenericIPAddressField
#NullBooleanField
#PositiveIntegerField
#PositiveSmallIntegerField
#SlugField
#SmallIntegerField
#TextField
#TimeField
#URLField
#UUIDField
#ForeignKey
#ManyToManyField
#OneToOneField
#

#这个模形用来存储用户能够访问的区域和设备的key
class UserAccessM(models.Model):
	user = models.ForeignKey(User,verbose_name = (u'用户'))  #一个用户可以对多个设备或者区域进行访问
	region_or_dev_flag = models.BooleanField(verbose_name=(u'区域'))        #为真则表示是区域访问权限，为假则表示是设备访问权限
	region_access_key = models.CharField(max_length = 40,verbose_name=(u'密钥'))#保存设备访问权限的access_key
	#下面这两个值跟安装的设备的具体区域代码和设备代码有关系
	region_id = models.SmallIntegerField(verbose_name=(u'区域编号'))    #Values from -32768 to 32767 are safe in all databases supported by Django.
	dev_id = models.BigIntegerField(verbose_name=(u'设备编号')) #numbers from -9223372036854775808 to 9223372036854775807
	#下面的是对设备的基本操作权限的设定
	permission_w = models.BooleanField(default=False,verbose_name=(u'写权限'))  #写和修改的权限
	permission_r = models.BooleanField(default=False,verbose_name=(u'读权限'))	  #读的权限
	permission_c = models.BooleanField(default=False,verbose_name=(u'控制权限'))    #控制的权限
	date_time = models.DateTimeField(default=timezone.now,verbose_name=(u'修改时间'))
	def __unicode__(self):
		return  str(self.id)
class UserAAdmin(admin.ModelAdmin):
	list_display=('user','region_or_dev_flag','date_time')
#这个模型用来存储基本的用户扩展信息	
class UserProfileM(models.Model):

	user = models.OneToOneField(User,unique = True,verbose_name = ('用户'))
	phone = models.CharField(max_length = 20,verbose_name=(u'电话号码'))
	job = models.CharField(max_length = 50,blank=True,verbose_name=(u'职位'))         
	section= models.CharField(max_length = 50,blank=True,verbose_name=(u'部门')) 
	job_unit = models.CharField(max_length = 50,blank=True,verbose_name=(u'单位')) 
	def  __unicode__(self):
		return  u'配置文件'

	@models.permalink
	def get_absolute_url(self):
		return ('userprofiledetail',None,{'pk':str(self.id)})
class UserPAdmin(admin.ModelAdmin):
	list_display=('user','phone','job')


# Create your models here.
#Define region model
class  RegionM(models.Model):
	region_id = models.PositiveIntegerField(unique = True,verbose_name=("区域编号"))
	region_info = models.CharField(max_length=50,blank=True,verbose_name=(u'区域描述'))
	region_name = models.CharField(max_length=50,blank=True,verbose_name=(u'区域名称'))
	reserved = models.CharField(max_length=50,blank=True,verbose_name=(u'保留项'))
	access_key = models.CharField(max_length=32,blank=True,verbose_name=(u'访问Key'))
	date_time = models.DateTimeField(default=timezone.now,verbose_name=(u'修改时间'))
	def __unicode__(self):
		return str(self.region_id)
class RegionAdmin(admin.ModelAdmin):
	list_display=('region_id','region_name','date_time')
class DevM(models.Model):
	dev_id = models.PositiveIntegerField(unique = True,verbose_name=(u'设备编号'))
	dev_info = models.CharField(max_length= 200,blank=True,verbose_name=(u'设备描述'))
	region  = models.ForeignKey(RegionM,verbose_name=(u'所属区域'))
	dev_name = models.CharField(max_length=50,blank=True,verbose_name=(u'设备名称'))
	access_key = models.CharField(max_length=32,blank=True,verbose_name=(u'访问Key'))
	dev_sn	=  models.CharField(max_length=48,blank=True,verbose_name=(u'设备序列号'))
	date_time = models.DateTimeField(default=timezone.now,verbose_name=(u'修改时间'))
	def __unicode__(self):
		return str(self.dev_id)
class DevAdmin(admin.ModelAdmin):
	list_display=('dev_id','dev_name','access_key')

SENSOR_TYPE=(
		('A',u'电流'),
		('V',u'电压'),
		('T',u'温度'),
		('H',u'湿度'),
		('P',u'压力'),
		('L',u'位置'),
		('Y',u'时间'),
		('F',u'文件'),
		('I',u'消息'),
		('J',u'图片'),
	)

class SensorM(models.Model):
	sensor_id = models.PositiveIntegerField(unique = True,verbose_name=(u'传感器编号'))
	sensor_info = models.CharField(max_length=200,blank=True,verbose_name=(u'传感器描述'))
	dev = models.ForeignKey(DevM,verbose_name=(u'传感器所属设备'))
	sensor_type = models.CharField(max_length = 10,choices=SENSOR_TYPE,verbose_name=(u'传感器类型'))
	sensor_name = models.CharField(max_length=50,blank=True,verbose_name=(u'传感器名称'))
	date_time = models.DateTimeField(default=timezone.now,verbose_name=(u'修改时间'))
	def __unicode__(self):
		return str(self.sensor_id)
class SensorAdmin(admin.ModelAdmin):
	list_display=('sensor_id','sensor_type','sensor_name','dev')
class DataM(models.Model):
	date_time = models.DateTimeField(default=timezone.now,verbose_name=(u'采集时间'))
	data = models.FloatField(verbose_name=(u'数据'))
	sensor  = models.ForeignKey(SensorM,verbose_name=(u'数据所属设备'))
class DataAdmin(admin.ModelAdmin):
	pass
class SensorThresholdM(models.Model):
	user = models.ForeignKey(User,verbose_name=(u'所属访问权限文件'))
	sensor_id = models.IntegerField(default=0,verbose_name=(u'传感器编号'))
	threshold_flag = models.BooleanField(default=True,verbose_name=(u'限值标志'))
	threshold = models.DecimalField(max_digits=6,decimal_places=2,default=10,verbose_name=(u'限值'))
	threshold_e = models.BooleanField(default=False,verbose_name=(u'使能位'))
class SensorTAdmin(admin.ModelAdmin):
	list_display=('threshold_flag','threshold','threshold_e')

class UserDevM(models.Model):

	useraccess = models.ManyToManyField(UserAccessM,verbose_name = ('用户'))
	first_name =  models.CharField(max_length = 20,verbose_name=(u'用户名'))
	last_name =  models.CharField(max_length = 20,verbose_name=(u'用户姓'))
	phone = models.CharField(max_length = 20,verbose_name=(u'电话号码'))
	email  = models.EmailField(verbose_name=(u'Email'))
	def  __unicode__(self):
		return  u'文件'
admin.site.register(UserProfileM,UserPAdmin)
admin.site.register(UserAccessM,UserAAdmin)
admin.site.register(SensorM,SensorAdmin)
admin.site.register(DevM,DevAdmin)
admin.site.register(RegionM,RegionAdmin)
admin.site.register(SensorThresholdM,SensorTAdmin)
admin.site.register([DataM,UserDevM])
