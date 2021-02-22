"""mycoffee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    
    path('grappelli/',include('grappelli.urls')) , 
   
    path('admin/', admin.site.urls),
    path('',include('pages.urls')),
    path('accounts/',include('accounts.urls')),
    path('products/',include('products.urls')),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT )


urlpatterns += i18n_patterns(    
    # accounts (django.contrib.auth.urls)
   
   # path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    
   # path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('accounts/change_password', auth_views.PasswordChangeView.as_view(template_name='accounts/change_password.html'), name='password_change'),
   
    path('accounts/change_password/done', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/change_password_done.html'), name='password_change_done'),
    
   # path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
   
  #  path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
   
   # path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
  #  path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    prefix_default_language=False,
)