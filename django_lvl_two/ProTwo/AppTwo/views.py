from django.shortcuts import render
from django.http import HttpResponse

from AppTwo.models import User

# Create your views here.
def index(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    help_dict = {'hey': 'Help Page'}
    return render(request, 'AppTwo/help.html', context=help_dict)

def users(request):
    users_list = User.objects.all()
    users_dict = {'users': users_list}
    return render(request, 'AppTwo/users.html', context=users_dict)
