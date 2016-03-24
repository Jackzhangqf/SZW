from django.shortcuts import render

from django.template import loader,Context,response
from django.http import HttpResponse
from blog.models import BlogPost,UserForm
from blog.forms import *
from django.contrib.auth import authenticate

def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("archive.html")
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))
 
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print request.path
        #form_d = request.POST.copy()
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                print 'login '
        #coocie = request.COOKIES
        #print coocie.items()
        form = UserForm(request.POST)
        if not form.is_valid():
            print "is invalid!"
        else:
            print "is valid!"
        return HttpResponse("It's OK!")
    else:
        form = UserForm()
        #t = loader.get_template('forms.html')
        c = Context({'form': form})
        return response.TemplateResponse(request,'forms.html',{'form':form})

# Create your views here.
