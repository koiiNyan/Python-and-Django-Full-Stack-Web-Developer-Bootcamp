from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileForm

# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

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
