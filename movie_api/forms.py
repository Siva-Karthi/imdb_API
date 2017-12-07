from django import forms
from django.contrib.auth import (
     authenticate,
     get_user_model,
     login,
     logout,
)

User = get_user_model()

class UserLoginForm(forms.Form):
   username = forms.CharField()
   password = forms.CharField(widget=forms.PasswordInput) 
  
   # def __init__(self, request=None, *args, **kwargs):
   #      """
   #      If request is passed in, the form will validate that cookies are
   #      enabled. Note that the request (a HttpRequest object) must have set a
   #      cookie with the key TEST_COOKIE_NAME and value TEST_COOKIE_VALUE before
   #      running this validation.
   #      """
   #      self.request = request
   #      self.user_cache = None
   #      print "init req"
   #      super(UserLoginForm, self).__init__(*args, **kwargs)
 
   def clean(self,*args,**kwargs):
       print "clean calles"
       username = self.cleaned_data.get("username")
       password = self.cleaned_data.get("password")
       
       user = authenticate(username=username, password=password)
       if username and password:
           if not user:
                raise forms.ValidationError("This user does not exist")
           if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
           if not user.is_active:
                raise forms.ValidationError("This user is not longer active")
       return super(UserLoginForm, self).clean(*args, **kwargs)
            

