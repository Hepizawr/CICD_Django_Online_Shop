from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from orders.models import Basket


# Create your views here.
def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index:index'))
    else:
        form = UserLoginForm()
    context = {
        'title': "Famms - login",
        'form': form
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration was successful")
            return HttpResponseRedirect(reverse('user:login'))
    else:
        form = UserRegistrationForm()
    context = {
        'title': "Famms - registration",
        'form': form
    }
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    if request.method == "POST":
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'title': "Famms - profile",
        'form': form,
        'basket': Basket.objects.filter(user=request.user)
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("index:index"))
