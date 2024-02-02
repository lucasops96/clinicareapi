from django import forms 


class LoginForm(forms.Form):

    email = forms.EmailField(
        label='E-mail',
        widget=forms.EmailInput(attrs={'placeholder':'Digite seu e-mail'}),
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'placeholder':'Digite sua senha'}),
    )