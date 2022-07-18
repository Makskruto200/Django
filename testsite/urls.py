"""testsite URL Configuration

__________________________________________                                                                       
TESTSITE
ПУТИ К СТРАНИЦАМ                                                                                                  
_________________________________________
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('blog.urls'))
]

