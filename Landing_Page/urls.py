from django.urls import include, path
from . import views
import events

urlpatterns = [
    path('', views.Startpagina),
    path('<int:url_id>/', events.views.Event_read),
    path('archief/', events.views.archief),

]