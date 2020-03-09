
from django.urls import path

from . import views
from events.views import Event

urlpatterns = [
    path('<int:url_id>/', views.index)

]
