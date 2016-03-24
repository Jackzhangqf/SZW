
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
#If you're using Django from an external script,
# you have to run django.setup() before you use any of the 
# models
import django
django.setup()
#os.environ.setdefault("DJANGO_SETTINGS_MODULE","mysite.settings")
from django.contrib.auth import authenticate
user = authenticate(username='blog',password='blogblog')
if user is not None:
    #the password verified for the user
    if user.is_active:
    	print('User is valid,active and authenticated')
    else:
    	print('The password is valid,but the account has been disabled!')
else:
	# Hte authentication system was unable to verify the username and password
	print('The username and password were incorrect.')
