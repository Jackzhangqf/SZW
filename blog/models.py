from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import Permission,User 
from django.contrib import admin
from django.forms import ModelForm,TextInput
from suit.widgets import SuitSplitDateTimeWidget

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ('-timestamp',)

class Contact(models.Model):
    name = models.CharField(max_length=200)
    age  = models.IntegerField(default=0)
    email = models.EmailField()
    def __unicode__(self):
        return self.name
class Tag(models.Model):
    contact = models.ForeignKey(Contact)
    name = models.CharField(max_length=50)
    def __unicode__(self):
    	return self.name

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']

class BlogPostForm(ModelForm):
    class Meta:
    	model = BlogPost
    	fields = '__all__'
        widgets = {
            'body': TextInput(attrs = {'class': 'input-mini'}),
            'timestamp': SuitSplitDateTimeWidget,
        }
class BlogPostAdmin(admin.ModelAdmin):
    form = BlogPostForm
    list_display = ('title','timestamp')
    fieldsets = (
         ['Main',{
             'fields':('title','timestamp'),
         }],
         ['Advance',{
             'classes':('collapse',),#CSS
             'fields':('body',),
         }]
    	)
class TagInline(admin.TabularInline):
	model = Tag

class ContactAdmin(admin.ModelAdmin):
	inlines = [TagInline] #Inline
	fieldsets = (
        ['Main',{
            'fields':('name','email'),
            }],
        ['Advance',{
            'classes':('collapse',),
            'fields':('age',),
        }]
		)

admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register([Tag])

