from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request, 'contact2.html')

def home(request):
    return render(request, 'index.html')