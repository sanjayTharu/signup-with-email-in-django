from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        dateofbirth=request.POST.get('birthdate')
        password=request.POST.get('password1')
        password2=request.POST.get('password2')

        print(uname)
        print(email)
        print(dateofbirth)
        print(password)
        print(password2)

        user=User.objects.filter(username=email)
        
        if user.exists():
            messages.info(request,'Email already Exists ')
            return redirect('/register/')

        if password !=password2:
            messages.info(request, 'Password and confirm password didnot match ' )
            return redirect('/register/')
        else:
            user=User.objects.create_user(
                username=email
            )
            user.set_password(password)
            user.save()

            messages.info(request,'Account Created Successfully')


        return redirect('/login/')



    return render(request,'register/register.html')