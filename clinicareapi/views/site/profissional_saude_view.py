from django.views.generic import CreateView
from ...models import ProfissionalSaude
from ...forms.profissional_form import ProfissionalSaudeForm

class ProfissionalSaudeCreateView(CreateView):
    template_name = 'profissional/profissional_saude_create_view.html'
    model = ProfissionalSaude
    form_class = ProfissionalSaudeForm
    