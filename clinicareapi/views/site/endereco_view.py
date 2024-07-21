from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from ...models import Endereco, ProfissionalSaude, Paciente
from ...forms.endereco_form import EnderecoForm

class EnderecoListView(ListView):
    template_name = 'endereco/endereco_list_view.html'
    model = Endereco

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.user_custom.is_profissional_saude:
            qs = ProfissionalSaude.objects.filter(id=self.request.user.user_custom.id_profissional).first().enderecos_atendimento.all()
        else:
            qs = Paciente.objects.filter(id=self.request.user.user_custom.id_paciente).first().endereco
        return qs
    

class EnderecoCreateView(CreateView):
    template_name = 'endereco/endereco_create_view.html'
    model = Endereco
    form_class = EnderecoForm

    def post(self,request,*args, **kwargs):
        if self.request.user.user_custom.is_profissional_saude:
            endereco = EnderecoForm(request.POST)
            if endereco.is_valid():
                endereco = Endereco.objects.create(**endereco.cleaned_data)
                endereco.cidade = endereco.cidade.upper()
                endereco.estado = endereco.estado.upper() 
                endereco.save()
                profissional = ProfissionalSaude.objects.filter(id=self.request.user.user_custom.id_profissional).first()
                profissional.enderecos_atendimento.add(endereco.pk)

                messages.success(request,'Endereço salvo com sucesso!')
            else:
                messages.error(request,'Verifique os campos do endereço!')
                return HttpResponseRedirect(reverse('clinicareapi:endereco_create'))

        return HttpResponseRedirect(reverse('clinicareapi:endereco_list'))

class EnderecoUpdateView(UpdateView):
    template_name = 'endereco/endereco_update_view.html'
    model = Endereco
    form_class = EnderecoForm

    def get_success_url(self):
        messages.success(self.request,'Endereço editado com sucesso!')
        return reverse('clinicareapi:endereco_list')

    def form_valid(self, form):
        endereco = form.save(commit=False)
        endereco.cidade = endereco.cidade.upper()
        endereco.estado = endereco.estado.upper()
        return super().form_valid(form)   

class EnderecoDeleteView(DeleteView):
    template_name = 'endereco/endereco_delete_view.html'
    model = Endereco
    context_object_name = 'endereco'

    def get_success_url(self):
        messages.success(self.request,'Endereço excluído com sucesso!')
        return reverse('clinicareapi:endereco_list')