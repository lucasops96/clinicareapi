from typing import Any
from django.http import HttpRequest, HttpResponse
from django.views.generic import CreateView , ListView
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from ...models import ProfissionalSaude, CustomUser, User
from ...forms.profissional_form import ProfissionalSaudeForm
from ...forms.user_form import UserForm
from ...forms.custom_user_form import CustomUserForm

class ProfissionalSaudeListView(ListView):
    template_name = 'profissional/profissional_saude_list_view.html'
    model = ProfissionalSaude
    

class ProfissionalSaudeCreateView(CreateView):
    template_name = 'profissional/profissional_saude_create_view.html'
    model = ProfissionalSaude
    form_class = ProfissionalSaudeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_user"] = UserForm
        context["form_custom"] = CustomUserForm
        return context
    
    def post(self, request, *args, **kwargs):
        form_user = UserForm(request.POST)
        form_custom = CustomUserForm(request.POST)
        form = ProfissionalSaudeForm(request.POST)
        
        if form_user.is_valid() and form_custom.is_valid() and form.is_valid():
            user = form_user.save(commit=False)
            user.set_password(user.password)
            user.save()

            custom = form_custom.save(commit=False)
            custom_user = CustomUser.objects.create(
                user_custom=user,
                cpf=custom.cpf,
                telefone=custom.telefone,
                is_profissional_saude=True
            )

            profissional = form.save(commit=False)
            profissional.user_profissional = custom_user
            profissional.save()

            messages.success(request,'Usuário salvo com sucesso!')

            return redirect(
                reverse('clinicareapi:login')
            )
        
        return render(
            request,
            self.template_name,
            {
                'form_user': form_user,
                'form_custom': form_custom,
                'form': form,
            }
        )
    
    