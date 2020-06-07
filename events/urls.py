
from django.urls import include, path

from . import views
from .views import Testlistview, TestDetail

urlpatterns = [

    path("", Testlistview.as_view()),
    path("<pk>", TestDetail.as_view()),
]