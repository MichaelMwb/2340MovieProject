from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe
from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser

class CustomErrorList(ErrorList):
    def __str__(self):
        if not self:
            return ''
        return mark_safe(''.join([f'<div class="alert alert-danger" role="alert">{e}</div>' for e in self]))

class CustomUserCreationForm(UserCreationForm):
    birthdate = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'MM-DD-YYYY'
        }),
        input_formats=['%m-%d-%Y'],
        required=True
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'birthdate')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2', 'birthdate']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})

    def clean_birthdate(self):
        birthdate = self.cleaned_data.get('birthdate')
        if not birthdate:
            raise ValidationError('Date must be in the form MM-DD-YYYY')
        return birthdate
