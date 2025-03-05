from django.contrib.auth.password_validation import CommonPasswordValidator, NumericPasswordValidator
from django.core import validators
from django import forms


class RegisterForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'autocomplete': 'email'}),
        validators=[
            validators.MinLengthValidator(5),
            validators.MaxLengthValidator(100),
            validators.EmailValidator(message="Enter a valid email address."),
        ],
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'autocomplete': 'username'}),
        validators=[
            validators.MinLengthValidator(4, "Username must be at least 4 characters."),
            validators.MaxLengthValidator(30, "Username cannot exceed 30 characters."),
        ]
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password','autocomplete': 'password'}),
        validators=[
            validators.MinLengthValidator(12, "Password must be at least 12 characters."),
            validators.MaxLengthValidator(100),
            validators.RegexValidator(
                regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W_]).+$',
                message="Password must contain: 1 uppercase, 1 lowercase, 1 number, 1 special character"
            )
        ],
    )


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'autocomplete': 'email'}),
        validators=[
            validators.MinLengthValidator(5),
            validators.MaxLengthValidator(100),
            validators.EmailValidator(message="Enter a valid email address."),
        ],
        help_text="Enter a valid email address (max 100 characters min 5 characters)."
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'autocomplete': 'password'}),
        validators=[
            validators.MinLengthValidator(5),
            validators.MaxLengthValidator(100)
        ]
    )
