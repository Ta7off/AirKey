from django.shortcuts import render

from django.views.generic import CreateView

from contacts.forms import ContactForm
from contacts.models import ContactMessage


class ContactView(CreateView):
    model = ContactMessage
    form_class = ContactForm
    template_name = 'skeleton/contacts/contact_form.html'