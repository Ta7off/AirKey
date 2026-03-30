from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView

from contacts.forms import ContactForm
from contacts.models import ContactMessage


class ContactView(CreateView):
    model = ContactMessage
    form_class = ContactForm
    template_name = 'skeleton/contacts/contact_form.html'
    success_url = reverse_lazy('contact_success')

def contact_success(request):
    return render(request, 'skeleton/contacts/contact_form_success.html')