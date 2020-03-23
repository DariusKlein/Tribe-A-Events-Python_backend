
from django.urls import include, path

from . import views
from django.urls import re_path

urlpatterns = [
    path('<int:url_id>/', views.Event_read),
    path('', views.Startpagina),
    path('archief/', views.archief),

]