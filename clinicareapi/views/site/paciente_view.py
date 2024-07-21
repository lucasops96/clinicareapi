from django.views.generic import ListView,CreateView,UpdateView,DetailView
from django.contrib import messages 
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from ...models import Paciente,CustomUser
from ...forms import PacienteForm,UserForm,CustomUserForm


class PacienteCreateView(CreateView):
    template_name = 'paciente/paciente_create_view.html'
    model = Paciente
    form_class = PacienteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_user"] = UserForm
        context["form_custom"] = CustomUserForm
        return context
    
    def post(self,request):
        form_user = UserForm(request.POST)
        form_custom = CustomUserForm(request.POST)
        form = PacienteForm(request.POST)

        if form_user.is_valid() and form_custom.is_valid() and form.is_valid():
            user = form_user.save(commit=False)
            user.set_password(user.password)
            user.save()

            custom = form_custom.save(commit=False)
            custom.user_custom = user
            custom.save() 

            paciente = form.save(commit=False)
            paciente.user_paciente = custom
            paciente.save()

            messages.success(request,'Registro feito com sucesso!')

            return HttpResponseRedirect(reverse('clinicareapi:login'))
        
        return render(
            request,
            self.template_name,
            {
                'form_user':form_user,
                'form_custom':form_custom,
                'form':form
            }
        )



