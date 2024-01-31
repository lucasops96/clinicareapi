from django.views.generic import CreateView , ListView
from ...models import ProfissionalSaude, CustomUser, User
from ...forms.profissional_form import ProfissionalSaudeForm
from ...forms.user_form import UserForm

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
        return context
    
    