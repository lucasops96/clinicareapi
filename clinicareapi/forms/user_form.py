from django import forms 
from ..models import User
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    
    username =  forms.CharField(
        label='Username',
        error_messages={
            'required':'This field must not be empty'
        },
        widget= forms.TextInput(attrs={'placeholder':'Seu username'}),
        help_text=(
            'O nome de usuário deve conter letras, números ou um desses @.+-_.'
        ),
    )

    email = forms.EmailField(
        label='E-mail',
        help_text='O e-mail deve ser válido',
        widget= forms.EmailInput(attrs={'placeholder':'Seu e-mail'}),
        error_messages={'required': 'E-mail is required'},
    )

    first_name = forms.CharField(
        label='Primeiro Nome',
        error_messages={'required': 'Write your first name'},
        widget= forms.TextInput(attrs={'placeholder':'Ex.: Miguel'})
    )

    last_name = forms.CharField(
        label='Último Nome',
        error_messages={'required':'Write your last name'},
        widget= forms.TextInput(attrs={'placeholder':'Ex.: Silva'})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'Digite uma senha'}),
        label='Senha',
        error_messages={'required':'Password must not be empty'},
        help_text=(
            'A senha deve ter pelo menos uma letra maiúscula,  '
            'uma letra minúscula e um número. Com a quantidade'
            'de pelo menos 8 caracteres.'
        ),
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'Repita sua senha'}),
        label='Confirme sua Senha',
        error_messages={
            'required':'Please, repeat your password'
        },
    )
    
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email','')
        user  = User.objects.filter(email=email).exists()

        if user:
            self.add_error('email','Este e-mail está em uso por outro Usuário.')

        return email
    
    def clean(self):
        clean_data = super().clean()

        password = clean_data.get('password')
        password2 = clean_data.get('password2')
        
        if password != password2:
            self.add_error('password','Senha deve ser igual Confirme sua Senha.')