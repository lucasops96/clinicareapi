from django import forms
from ..models import ProfissionalSaude

class ProfissionalSaudeForm(forms.ModelForm):

    class Meta:
        model = ProfissionalSaude
        fields = ['especialidade', 'conselho', 'numero_conselho']
        exclude = ['user_profissional']
        labels = {
            'especialidade':'Especialidade',
            'conselho':'Conselho',
            'numero_conselho':'N° Conselho'
        }
        widgets = {
            'especialidade':forms.TextInput(attrs={'required':True}),
            'numero_conselho':forms.TextInput(attrs={'required':True}),
        }