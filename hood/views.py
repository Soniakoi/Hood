from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required

# Create your views here.
def welcome(request):
  title = 'hood'
  return render(request, 'welcome.html',{"title":title})

@login_required(login_url='/accounts/login')
def hood(request,neighbourhood_id):
