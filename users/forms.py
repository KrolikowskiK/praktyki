from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from .models import CustomUser

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Row, Hidden


class CustomUserCreationForm(UserCreationForm):
    """
    Renders form for creating user with email and password credentials.
    Uses crispy_forms for managing form look.
    """
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(help_text=None, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(help_text=None, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.attrs = {'novalidate': ''}
        self.helper.layout = Layout(
            Row(Field('email', css_class='form-control'), css_class='mb-3'),
            Row(Field('password1', css_class='form-control'), css_class='mb-3'),
            Row(Field('password2', css_class='form-control'), css_class='mb-3'),
            Row(Submit('submit', 'Sign up'), css_class='mb-1')
        )

    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class CustomUserAuthenticationForm(AuthenticationForm):
    """
    Renders authentication form with username as email and password fields.
    Uses crispy_forms for managing form look.
    """
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Email'}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'placeholder': 'Password'}),
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        self.helper.attrs = {'novalidate': ''}
        self.helper.layout = Layout(
            Row(Field('username', css_class='form-control'), css_class='mb-3'),
            Row(Field('password', css_class='form-control'), css_class='mb-3'),
            Row(Submit('submit', 'Sign in'), css_class='mb-1'),
            Hidden('next', '{{ next }}')
        )
