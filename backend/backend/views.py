from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.mail import send_mail
from rest_framework.response import Response
from django.conf import settings
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,'index.html')