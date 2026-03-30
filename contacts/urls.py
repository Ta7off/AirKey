from django.urls import path

from contacts.views import ContactView, contact_success

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact_us'),
    path('success/', contact_success, name='contact_success'),
]
