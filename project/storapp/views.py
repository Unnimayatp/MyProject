from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect




# Create your views here.



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('personform_page')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, 'login.html')




def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cnpassword = request.POST['cnpassword']
        if password == cnpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email, password=password)
                user.save();
                print('user created')




        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('login')

    return render(request, 'register.html')







