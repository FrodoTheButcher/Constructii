from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.mail import send_mail
from rest_framework.response import Response
from django.conf import settings
from django.shortcuts import render
# Create your views here.


@api_view(['POST'])
def Contact(request):
     if request.method=='POST':
        body=request.data.get('body')
        gmail=request.data.get('gmail')
        fullname=request.data.get('fullname')
        phone=request.data.get('phone')
        body= "message from "+ fullname + " with the phone number :  "+ phone +" and the message : "+body
        try:
            print(body+" gmail: "+gmail)
            send_mail(fullname, body, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
        except:
            return Response("email not send...")

        return Response("success")