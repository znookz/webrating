from django.shortcuts import render,redirect
from django.contrib import messages
from .models import ratingtb
from django.contrib.auth.models import User,auth

# Create your views here.

def mainpage(request):
    return render(request,'index.html')

def votepage(request):
    return render(request,'index.html')

def voterecord(request):
    scorevote = request.POST['scorevote']
    event1 = ratingtb(scorerating=scorevote)        
    event1.save()
    return redirect('/')
    
def loginpage(request):
    return render(request,'loginpage.html')

def managerpage(request):

    username=request.POST['username']
    password=request.POST['password']

    user = auth.authenticate(username=username,password=password)

    if user is not None :
        auth.login(request,user)
        return render(request,'managerpage.html')
    else :
        messages.info(request,'Username หรือ Password ไม่ถูกต้อง')

    return redirect('/loginpage')

