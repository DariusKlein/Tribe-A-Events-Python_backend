from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View


class Index(View):
    template = 'index.html'

    def get(self, request):
        return render(request, self.template)




class page1(View):
    template = 'page1.html'

    def get(self, request):
        return render(request, self.template)
