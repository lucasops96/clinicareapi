from django import forms
from ..models import ProfissionalSaude

class ProfissionalSaudeForm(forms.ModelForm):
    class Meta:
        model = ProfissionalSaude
        fields = 'user_profissional','especialidade', 'conselho', 'numero_conselho'
        labels = {
            'especialidade':'Especialidade:',
            'conselho':'Conselho:',
            'numero_conselho':'N° Conselho:'
        }
        widgets = {
            'conselho': forms.Select(
                choices=(
                    ('CRO','CRO'),
                    ('CRM','CRM'),
                    ('CREFITO','CREFITO'),
                    ('CREF','CREF'),
                ),
            ),
        }