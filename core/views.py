from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request, 'contact.html')


def home(request):
    return render(request, 'index.html')