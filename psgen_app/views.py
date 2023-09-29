from django.shortcuts import render
from django.http import *
import random

# Create your views here.

def index_view(request):
    return render(request, 'index.html')

def home_view(request):
    return render(request, "home.html")

def passgen_view(request):
    strg  = list('')
    if request.GET.get('LowerCase'):
        strg.extend(list('abcdefghijklmnopqrstuvwxyz'))
    if request.GET.get('UpperCase'):
        strg.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Number'):
        strg.extend(list('0123456789'))
    
    length = int(request.GET.get("length"))
    pswdgen = ""
    for i in range(length):
        pswdgen+= random.choice(strg)
        
    return render(request, "passgen.html", {"pswdgen": pswdgen})