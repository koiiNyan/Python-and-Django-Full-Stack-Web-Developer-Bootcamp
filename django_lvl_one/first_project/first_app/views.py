from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Each view is going to have at least one argument.
# Each view must return an HTTP Response Obj.

def index(request):
    my_dict = {'insert_me':"Now I'm coming from first_app/index.html ! "}
    return render(request, 'first_app/index.html',context=my_dict)
