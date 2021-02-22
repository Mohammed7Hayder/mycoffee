from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import SignUpForm
from django.views.generic import View
# Create your views here.

def signin(request):
    return render(request,'accounts/signin.html')








#'''''''''''''''
# def signup(request):
#        form = SignUpForm()
 #   if request.method =='POST':
  #      form =SignUpForm (request.POST)
  #      if form.is_valid():
   #         user = form.save()
    #        auth_login(request,user)
            
     #       return redirect ('index')
    
   # return render(request,'accounts/signup.html',{'form':form})
#'''''''''''
class ContactView( View ):
   
        def get(self, request, *args, **kwargs):
            
            form = SignUpForm()
            return render(request, 'accounts/signup.html')

        def post(self, request, *args, **kwargs):
            if  request.method == 'POST':
                form = SignUpForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    auth_login(request,user)           
            
                    return redirect('index')
        
                return render(request,'accounts/signup.html',{'form':form})




















 
def profile(request):
    return render(request , 'accounts/profile.html')