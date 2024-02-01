from django import forms 
from ..models import CustomUser

class CustomUserForm(forms.ModelForm):
    cpf = forms.CharField(
        label='CPF',
        error_messages={
            'required':'Type your CPF'
        },
        widget=forms.TextInput(attrs={'placeholder':'000.000.000-00'})
    )

    telefone = forms.CharField(
        label='WhatsApp',
        error_messages={
            'required':'Type your WhatsApp'
        },
        widget=forms.TextInput(attrs={'placeholder':'(00) 00000-0000'})
    )

    class Meta:
        model = CustomUser
        fields = [
            'cpf',
            'telefone',
            'is_profissional_saude'
        ]
    
    