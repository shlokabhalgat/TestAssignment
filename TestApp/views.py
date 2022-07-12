from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import NewUserForm, ThoughtPostedByUser
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .models import *


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:thought_post")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("main:login")


def homepage(request):
    return render(request=request, template_name='homepage.html')


@login_required
def post_create(request):
    form = ThoughtPostedByUser(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            # add user to the instance ↓
            form.instance.user = request.user
            form.save()
            messages.success(request, 'Your post was successfully created!')
            return redirect('main:dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ThoughtPostedByUser()
    return render(request, "thought_post.html", context={"post_form": form})

@login_required
def view_posts(request):
    post_object = ThoughtPostModel.objects.all()
    print(post_object)
    return render(request,"dashboard.html",context={"all_posts": post_object})
