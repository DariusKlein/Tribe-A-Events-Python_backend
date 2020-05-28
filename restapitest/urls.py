from django.urls import path

from .views import Testlistview, TestDetail


urlpatterns = [
    path("", Testlistview.as_view()),
    path("<pk>", TestDetail.as_view()),
]