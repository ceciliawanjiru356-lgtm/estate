from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html') 

def services(request):
    return render(request, 'services.html')   

def properties(request):
    return render(request, 'properties.html')

def agents(request):
    return render(request, 'agents.html')

def contact(request):
    return render(request, 'contact.html')

