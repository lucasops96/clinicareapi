from django import forms 
from ..models import User
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    
    username =  forms.CharField(
        label='Username',
        error_messages={
            'required':'This field must not be empty'
        },
        widget= forms.TextInput(attrs={'placeholder':'Your username'}),
        help_text=(
            'Username must have letters, numbers or one of those @.+-_. '
        ),
    )

    email = forms.EmailField(
        label='E-mail',
        help_text='The e-mail must be valid',
        widget= forms.EmailInput(attrs={'placeholder':'Your e-mail'}),
        error_messages={'required': 'E-mail is required'},
    )

    first_name = forms.CharField(
        label='First Name',
        error_messages={'required': 'Write your first name'},
        widget= forms.TextInput(attrs={'placeholder':'Ex.: Miguel'})
    )

    last_name = forms.CharField(
        label='Last Name',
        error_messages={'required':'Write your last name'},
        widget= forms.TextInput(attrs={'placeholder':'Ex.: Silva'})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'Type your password'}),
        label='Password',
        error_messages={'required':'Password must not be empty'},
        help_text=(
            'Password must have at least one uppercase letter, '
            'one lowercase letter and one number. The length should be '
            'at least 8 characters.'
        ),
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'Repeat your password'}),
        label='Confirm Password',
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
            raise ValidationError(
                'User e-mail is already in use',code='invalid',
            )
        
        return email
    
    def clean(self):
        clean_data = super().clean()

        password = clean_data.get('password')
        password2 = clean_data.get('password2')
        
        if password != password2:
            password_error = ValidationError(
                'Password and Confirm Password must be equal'
            )

            raise ValidationError({
                'password':password_error,
                'password2':[
                    password_error,
                ],
            })