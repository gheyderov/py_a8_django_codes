from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from core.forms import ContactForm
from django.contrib import messages
from django.views.generic import CreateView
from django.utils.translation import gettext_lazy as _
from core.tasks import export_data

def export(request):
    export_data.delay()
    return HttpResponse('Success!')


# Create your views here.

class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.add_message(self.request, messages.SUCCESS, _("Successfully sent!"))
        return super().form_valid(form)

# def contact(request):
#     form = ContactForm()

#     if request.method == 'POST':
#         form = ContactForm(data = request.POST)
#         if form.is_valid():
#             form.save()
#             messages.add_message(request, messages.SUCCESS, "Successfully sent!")
#             return redirect(reverse_lazy('contact'))
#     context = {
#         'form' : form
#      }
#     return render(request, 'contact.html', context)


def home(request):
    return render(request, 'index.html')