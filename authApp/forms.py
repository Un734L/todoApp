from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    passwordConfirm=forms.CharField(widget=forms.PasswordInput,label='Confirm Password:')
    class Meta:
        model =User 
        fields = [
            'username',
            'email',
            'password',
        ]
    def clean(self):
        cleaned_data=super().clean()

        password=cleaned_data.get('password')
        passwordConfirm=cleaned_data.get('passwordConfirm')

        if password!=passwordConfirm:
            raise forms.ValidationError('Passwords do not match.')
        return cleaned_data

