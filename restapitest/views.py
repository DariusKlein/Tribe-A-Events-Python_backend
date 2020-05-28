from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Test
from .serializers import testserializer


# Create your views here.

class Testlistview(ListAPIView):
    queryset = Test.objects.all()
    serializer_class = testserializer


class TestDetail(RetrieveAPIView):
    queryset = Test.objects.all()
    serializer_class = testserializer
