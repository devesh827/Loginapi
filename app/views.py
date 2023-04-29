from django.shortcuts import render,redirect
from django.views import View
from .forms import CustomerRegistrationForm
from django.contrib import messages
from django.shortcuts import render
from rest_framework import viewsets
from app.models import User
from app.serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class CustomerRegistrationView(View):
  def get(self,request):
    form=CustomerRegistrationForm()
    return render(request, 'app/customerregistration.html',{'form':form})
  def post(self,request):
    form=CustomerRegistrationForm(request.POST)
    if form.is_valid():
       messages.success(request,"user created successfully")
       form.save()
       return redirect("login")


def logindone(request):
   return render(request,'app/logindone.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    
