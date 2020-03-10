
from django.urls import path

from . import views

urlpatterns = [
    path('<int:url_id>/', views.Event_read),
    path('', views.Startpagina)

]
