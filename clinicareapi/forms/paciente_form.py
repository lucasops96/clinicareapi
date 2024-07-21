from django import forms
from ..models import Paciente


class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        exclude = ['endereco','user_paciente']
        labels = {
            'peso':'Peso (em kg)'
        }
        widgets = {
            'idade':forms.NumberInput(attrs={'required':True}),
            'sexo':forms.TextInput(attrs={'required':True}),
            'peso':forms.NumberInput(attrs={'required':True})
        }