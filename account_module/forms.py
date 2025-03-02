from django.core import validators
from django import forms


class RegisterForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
