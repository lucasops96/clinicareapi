from django import forms
from ..models import ProfissionalSaude

class ProfissionalSaudeForm(forms.ModelForm):
    class Meta:
        model = ProfissionalSaude
        fields = 'user_profissional','especialidade', 'conselho', 'numero_conselho'