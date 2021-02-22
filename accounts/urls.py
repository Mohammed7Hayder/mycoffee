from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from mycoffee import settings
urlpatterns = [
  # path('signin', views.signin, name = 'signin' ),
   # path('signup', views.signup, name = 'signup'),
    path('signup', views.ContactView.as_view(), name='signup'),
    path('logout', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    
    path('signin', auth_views.LoginView.as_view(template_name='accounts\signin.html' ), name='signin'),
  #  path('login/',auth_views.LoginView.as_view(template_name= 'login.html'),name = 'login'),
   
   
    path('profile',views.profile,name = 'profile' ),
]
