from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Saving directly to DB
            user = user_form.save()
            # Hashing pass
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            # Setting the relationship
            profile.user = user

            # checks if provided a profile pic
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    # if request.method == 'GET':
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'basic_app/registration.html',
                                {'user_form':user_form,
                                'profile_form':profile_form,
                                'registered':registered})




def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print("Someone tried to login and failed!")
            print(f"Username: {username} and password: {password}")
            return HttpResponse("Invalid login detailes supplied!")
    else:
        return render(request,'basic_app/login.html')
