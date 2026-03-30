from django.shortcuts import render

from contacts.views import ContactView

def IndexView(request):
    return render(request, "index.html")
