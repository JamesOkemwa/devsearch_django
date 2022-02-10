from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

def loginUser(request):

    # restrict logged in user from seeing login page
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password) # queries the db. returns the user instance if the credentiials match. Else return None

        if user is not None:
            login(request, user) # creates a session for the user in the database
            return redirect('profiles')
        else:
            messages.error(request, 'Username or password is incorrect')


    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.error(request, 'User was logged out')
    return redirect('login')


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)

    topSkills = profile.skill_set.exclude(description__exact="") # excludes skills without description
    otherSkills = profile.skill_set.filter(description="")

    context={'profile': profile, 'topSkills': topSkills, 'otherSkills': otherSkills}
    return render(request, 'users/user-profile.html', context)