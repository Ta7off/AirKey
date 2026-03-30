from django.shortcuts import render

from contacts.views import ContactView

def IndexView(request):
    return render(request, "skeleton/core/index.html")
