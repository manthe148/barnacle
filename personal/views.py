from django.shortcuts import render
from django.views import generic

# Create your views here.
def index(request):
    template_name = 'index.html'
    return render(request, template_name)
    