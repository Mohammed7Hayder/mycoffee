from django.urls import path
from . import views


urlpatterns = [            
    
    path('',views.index, name = 'index'),
    path('adout',views.about, name = 'adout'),
    path('coffee',views.coffee, name = 'coffee'),  
]
    