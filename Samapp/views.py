from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request,'home.html')

def thrissur_page(request):
    return render(request,'thrissur.html') 

def palakkad_page(request):
    return render(request,'palakkad.html') 

def kannur_page(request):
    return render(request,'kannur.html') 

def kozhikode_page(request):
    return render(request,'kozhikode.html') 

def wayanad_page(request):
    return render(request,'wayanad.html') 