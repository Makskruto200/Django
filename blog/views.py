"""
__________________________________________                                                                       
TESTSITE/BLOG                                               ПРЕДСТАВЛЕНИЕ СТРАНИЦ                          
_________________________________________
"""
from django.shortcuts import render,HttpResponse

def home(request):
    return render(request,"blog/home.html")

