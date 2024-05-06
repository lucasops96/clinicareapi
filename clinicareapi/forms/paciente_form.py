from django import forms
from ..models import Paciente


class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        exclude = ['endereco']
        labels = {
            'peso':'Peso (em kg)'
        }