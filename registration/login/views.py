from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.



def login_page(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        print(username)
        print(password)

        if not User.objects.filter(username=username).exists():
            messages.info(request,'Username doesnot exists')
            return redirect('/login/')
        
        user=authenticate(username=username,password=password)

        if user is None:
            messages.error(request,'Invalid Password')
            return redirect('/login/')


        else:
            login(request,user)
            return redirect('/home/')

    return render(request,'login/login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')