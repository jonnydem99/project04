from django.shortcuts import render

def home( request): 
    return render( request, 'stocktrader/home.html')

def about( request): 
    return render( request, 'stocktrader/about.html')