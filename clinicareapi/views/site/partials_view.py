from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ...models import User
from ...forms.login_form import LoginForm
from ...forms.user_form import UserPassword

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
    
    form = UserPassword()

    return render(request,'partials/senha.html',{
        'form':form
    })

def senha_alterada(request,pk):
    user = User.objects.filter(id=pk).first()

    if request.user.id != user.id or not request.POST:
        raise Http404()

    user_form = UserPassword(request.POST)

    if user_form.is_valid():
        print('-------------',user_form.cleaned_data.get('old_password',''))
        if user.check_password(user_form.old_password):
            user.set_password(user_form.new_password)
            messages.success(request,'Senha alterada com sucesso!')
        else:
            messages.error(request,'Senha atual incorreta')

        return render(request,'partials/senha.html',{
            'form': UserPassword()
        })
    
    return render(request,'partials/senha.html',{
        'form':user_form
    })
            
