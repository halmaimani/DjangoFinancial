from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext

# Create your views here.

def index(request):
    return render(request, 'financial/index.html')


