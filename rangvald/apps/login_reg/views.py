from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
def index(request):
  return render(request,"login_reg/login.html")
  return HttpResponse("this is the equivalent of @app.route('/')!")