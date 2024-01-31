from django.views.generic import CreateView , ListView
from ...models import ProfissionalSaude, CustomUser
from ...forms.profissional_form import ProfissionalSaudeForm


class ProfissionalSaudeListView(ListView):
    template_name = 'profissional/profissional_saude_list_view.html'
    model = ProfissionalSaude
    

class ProfissionalSaudeCreateView(CreateView):
    template_name = 'profissional/profissional_saude_create_view.html'
    model = ProfissionalSaude
    form_class = ProfissionalSaudeForm
    