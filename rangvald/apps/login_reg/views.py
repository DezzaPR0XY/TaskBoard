from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, HttpResponse
# Create your views here.


def index(request):
  return render(request,"login_reg/login.html")

def signup(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=raw_password)
      login(request, user)
      return redirect('home')
  else:
    form = UserCreationForm()
  return render(request, 'signup.html', {'form': form})

def register(request):
  is_valid = True
  
  return render(request, "login_reg/login.html")

def login(request):

  return render(request, "login_reg/login.html")
