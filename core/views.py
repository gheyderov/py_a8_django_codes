from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from core.forms import ContactForm
from django.contrib import messages


# Create your views here.

def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Successfully sent!")
            return redirect(reverse_lazy('contact'))
    context = {
        'form' : form
     }
    return render(request, 'contact.html', context)


def home(request):
    return render(request, 'index.html')