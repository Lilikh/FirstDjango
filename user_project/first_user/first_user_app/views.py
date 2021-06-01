from django.shortcuts import render
from django.http import HttpResponse
from .models import userProfile

# Create your views here.

def index(request):

    userProfiles= userProfile.objects.all()

    return render(request,'first_user_app/index.html',{"userProfiles":userProfiles})

def user(request):

    userProfiles= userProfile.objects.all()

    return render(request,'first_user_app/user.html',{"userProfiles":userProfiles})