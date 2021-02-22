from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import  User

 

class SignUpForm(forms.Form,UserCreationForm):
    
    
    
    email =  forms.CharField(max_length=255,required = True, widget = forms.EmailInput() )
    Address = forms.CharField(max_length=1024,required = True ,    )
    Address2 = forms.CharField(max_length=1024,required = True  ,  )
    zip_code = forms.IntegerField(required=True )
    City = forms.CharField(max_length=1024,required = True )
    State = forms.CharField( max_length=1024 ,required = True)
    is_agree = forms.BooleanField( )
    is_agree2 = forms.NullBooleanField()
   
    first_name= forms.CharField(max_length=100, )   
    last_name= forms.CharField(max_length=100,)   
   
    #password1 = forms.CharField(widget=forms.PasswordInput()) 
    #password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'} ))      

    #def clean(self):
    #    cleaned_data = super().clean()

   #     p1 = cleaned_data.get('password1')
   #     p2 = cleaned_data.get('password2')
   #     if p1 != p2:
   #         raise forms.ValidationError("Yor passwords don,t match , tray agen")
   #     return cleaned_data
        
            
        
    class Meta:
        model = User
        fields = {   'is_agree2' ,'is_agree'}
       # fields = { 'username' ,'email' ,'zip_code' ,'password2', 'password1','is_agree2' ,'is_agree','last_name','first_name' ,'Address2','Address', 'City','State' }
                  #  {   'username', 'email' ,'password2','password1'}'zip_code'  'Address'
        
        
    
    
    
    
    
    