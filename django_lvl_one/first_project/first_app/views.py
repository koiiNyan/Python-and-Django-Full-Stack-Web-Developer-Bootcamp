from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Each view is going to have at least one argument.
# Each view must return an HTTP Response Obj.

def index(request):
    return HttpResponse("Hello World")
