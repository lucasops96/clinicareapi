from django.views.generic import ListView,CreateView,UpdateView,DetailView
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
    



