
from django.urls import include, path

from . import views

urlpatterns = [
    path('', include('Landing_Page.urls')),
]