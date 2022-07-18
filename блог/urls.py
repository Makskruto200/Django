"""
__________________________________________                                                                       
TESTSITE/BLOG
ПУТИ К СТРАНИЦАМ                                                                                                  
________________________________________                                                                                          
"""
from django.urls import path 
from . import views

urlpatterns = [
    
    path("",views.home,name="home")
]
