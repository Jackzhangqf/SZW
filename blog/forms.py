from django import forms
from blog.models import *


class LoginForm(forms.ModelForm):
    #title = forms.CharField(max_length=150,required = True)
    #body = forms.CharField(widget = forms.Textarea,max_length=150,required = True)
    #timestamp = forms.TimeField(label='time',required = True)
    class Meta:
    	model = BlogPost
    	fields = "__all__"
    	