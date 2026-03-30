from . import views
from django.urls import path

from core.views import IndexView

urlpatterns = [
    path('home/', views.IndexView, name='index'),
]
