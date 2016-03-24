#coding=utf-8
#forms.py
from django import forms
from IoT.models import  *
INPUT_CLASS = {'class':'form-control col-md-7 col-xs-12'}
DISABLE_INPUT_CLASS = {'class':'form-control col-md-7 col-xs-12' ,'disabled':'disabled'}
READNOLY_INPUT_CLASS = {'class':'form-control col-md-7 col-xs-12','readonly':"readonly"}
CHECKBOX_CLASS = {'class':'form-control col-md-7 col-xs-12 pull-left'}
DATE_INPUT_CLASS = {'class':'date-picker  form-control col-md-7 col-xs-12'}
SELECT2_SINGLE_CLASS={'class':'select2_single  form-control col-md-7 col-xs-12','tabindex':"-1"}
SELECT2_GROUP_CLASS={'class':'select2_group  form-control col-md-7 col-xs-12'}
SELECT2_MULTIPLE_CLASS={'class':'select2_multiple  form-control col-md-7 col-xs-12'}
#UserProfileM
class  UserProfileForm(forms.ModelForm):
	
	def  __init__(self, user, *args, **kwargs):

		super(UserProfileForm,self).__init__(*args, **kwargs)
		self.fields['user'] = forms.ModelChoiceField(
			queryset = User.objects.filter(username=user.username),
			label = "用户",
			required = True,
			help_text = "只能为当前登录的用户",
			error_messages = { 'required': "必须选择一个有效用户"},
			empty_label = "----------",
			widget = forms.Select(attrs=SELECT2_SINGLE_CLASS),
			)
	phone = forms.CharField(
		required = True,
		label = "电话号码",
		help_text = "填写一个电话号码",
		error_messages = {'required': "请设置一个正确的电话号码"},
		widget = forms.TextInput(attrs = INPUT_CLASS),
		)
	job = forms.CharField(
		required = True,
		label = "工作岗位",
		error_messages = {'required': "请填写工作类型"},
		widget = forms.TextInput(attrs = INPUT_CLASS),
		)
	job_unit = forms.CharField(
		required = True,
		label = "工作单位",
		error_messages = {'required': "请填写工作单位"},
		widget = forms.TextInput(attrs = INPUT_CLASS),
		)
	section = forms.CharField(
		required = True,
		label = "部门",
		error_messages = {'required': "请填写工作部门"},
		widget = forms.TextInput(attrs = DATE_INPUT_CLASS),
		)
	class Meta:
		model = UserProfileM
		fields =  '__all__'
#UserAccessM
#RegionM
#DevM
#SensorM
#DataM
#SensorThresholdM
class  SensorThresholdForm(forms.ModelForm):
	def  __init__(self,*args, **kwargs):
		self.user = kwargs.pop('user')
		super(SensorThresholdForm,self).__init__(*args, **kwargs)
		
		self.fields['user'] = forms.ModelChoiceField(
			queryset = User.objects.filter(username=self.user.username),
			label = "用户",
			required = True,
			help_text = "",
			error_messages = { 'required': "必须选择一个有效的用户"},
			empty_label = "----------",
			widget = forms.Select(attrs=SELECT2_SINGLE_CLASS),
			)
		self.fields['sensor_id']= forms.IntegerField(
			required = False,
			label = "传感器编号",
			help_text = "已经自动选择，不需要修改",
			#empty_label = self.sensor_id,
			error_messages = {'required': "请设置该值","invalid":"该值无效，请重新输入"},
			widget = forms.NumberInput(attrs = READNOLY_INPUT_CLASS),
			)
	threshold_flag = forms.BooleanField(
		required = False,
		label = "阈值标志",
		help_text = "为真表示为上限，为假表示为下限",
		#empty_label = True,
		error_messages = {'required': "请设置该值"},
		widget = forms.CheckboxInput(attrs = CHECKBOX_CLASS),
		)
	 
	threshold = forms.DecimalField(
		required = True,
		label = "阈值",
		error_messages = {'required': "请填写阈值"},
		widget = forms.NumberInput(attrs = INPUT_CLASS),
		)
	threshold_e = forms.BooleanField(
		required = False,
		label = "是否使用该阈值",
		#empty_label = True,
		error_messages = {'required': "请"},
		widget = forms.CheckboxInput(attrs = CHECKBOX_CLASS),
		)
	class Meta:
		model = SensorThresholdM
		fields =  '__all__'
#UserDevM
class  TestForm(forms.Form):
	#region_id = models.PositiveIntegerField(verbose_name=("区域编号"))
	region_id = forms.IntegerField(label=u"区域编号",
		widget=forms.TextInput(attrs=INPUT_CLASS))
	#region_info = models.CharField(max_length=50,blank=True,verbose_name=(u'区域描述'))
	region_info = forms.CharField(max_length=50,label=u'区域描述',
		widget=forms.TextInput(attrs=INPUT_CLASS))

	#region_name = models.CharField(max_length=50,blank=True,verbose_name=(u'区域名称'))
	region_name = forms.CharField(max_length=50,label=u'区域名称',
		widget=forms.TextInput(attrs=INPUT_CLASS))
	#reserved = models.CharField(max_length=50,blank=True,verbose_name=(u'保留项'))
	reserved = forms.CharField(max_length=50,label=u'保留项',
		widget=forms.TextInput(attrs=INPUT_CLASS))

	#access_key = models.CharField(max_length=32,blank=True,verbose_name=(u'访问Key'))
	access_key = forms.CharField(max_length=32,label=u'访问Key',
		widget=forms.TextInput(attrs=INPUT_CLASS))
	#date_time = models.DateTimeField(default=timezone.now,verbose_name=(u'修改时间'))
	date_time = forms.DateTimeField(label=u'访问Key',
		widget=forms.DateTimeInput(attrs=INPUT_CLASS))
	class Meta:
		model = UserProfileM
		fields="__all__"

	auto_id = False
	def as_t(self):
		"Returns this form rendered as HTML <p>s."
		return self._html_output(
			normal_row='<div%(html_class_attr)s>%(label)s <div>%(field)s%(help_text)s</div></div>',
			error_row='%s',
			row_ender='</div>',
			help_text_html=' <span class="helptext">%s</span>',
			errors_on_separate_row=True)
	

