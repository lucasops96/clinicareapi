from django.shortcuts import render
from ...forms.login_form import LoginForm

def login(request):
    form = LoginForm()
    return render(request,'partials/login.html',{
        'form':form
    })