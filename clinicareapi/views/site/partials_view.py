from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ...forms.login_form import LoginForm

def login_view(request):
    form = LoginForm()
    return render(request,'partials/login.html',{
        'form':form
    })

def login_create(request):
    if not request.POST:
        raise Http404()
    
    form = LoginForm(request.POST)

    if form.is_valid():
        authenticate_user = authenticate(
            username=form.cleaned_data.get('username',''),
            password=form.cleaned_data.get('password',''),
        )

        if authenticate_user is not None:
            messages.success(request,'Login realizado com sucesso!')
            login(request,authenticate_user)
        else:
            messages.error(request,'Credenciais inválidas')
    else:
        messages.error(request,'Username ou Senha inválido')
    
    return redirect(reverse('clinicareapi:dashboard'))


@login_required(login_url='clinicareapi:login',redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        messages.error(request, 'Logout inválido')
        return redirect(reverse('clinicareapi:login'))
    
    logout(request)
    messages.success(request, 'Logout realizado')
    return redirect(reverse('clinicareapi:login'))

@login_required(login_url='clinicareapi:login',redirect_field_name='next')
def dashboard(request):
    return render(request,'partials/dashboard.html',{
        'consultas':[
            {
                'paciente':'Miguel',
                'data':'12/04/2024'
            },
            {
                'paciente':'Miguel',
                'data':'12/04/2024'
            },
            {
                'paciente':'Miguel',
                'data':'12/04/2024'
            },
            {
                'paciente':'Miguel',
                'data':'12/04/2024'
            },
            {
                'paciente':'Miguel',
                'data':'12/04/2024'
            },
        ],
    })


def alterar_senha(request,pk):
    return render(request,'partials/senha.html')