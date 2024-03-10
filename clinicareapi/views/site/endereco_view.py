from django.views.generic import CreateView, ListView
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