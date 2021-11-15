from django.contrib.auth import forms
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserCreationForm()  
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect(login)
        context = {'form':form}
        return render(request, 'accounts/register.html',context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        

        context = {}
        return render(request, 'accounts/login.html', context)

@login_required(login_url='/users/login/')
def homePage(request):
    context = {}
    return render(request, 'accounts/homepage.html', context)

@login_required()
def logoutPage(request):
    logout(request)
    return redirect('login')