from django import forms
from django.core import validators
from . import models
from django.contrib.auth.models import User

# 
def myValidator(value):
    if value[0] != "Z":
        raise forms.ValidationError("ERRORRRRRR!")

class UserForm(forms.Form):
    first_name = forms.CharField(validators=[myValidator])
    last_name = forms.CharField()
    email = forms.EmailField()
    ver_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea, required=False)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        ver_email = all_clean_data['ver_email']

        if email != ver_email:
            raise forms.ValidationError("Make sure the email matches!")
        else:
            print('FINE') 

class IssueDescriptionForm(forms.ModelForm):
    """Form definition for IsseuDescription."""
    date = forms.DateField(widget=forms.DateTimeInput(attrs={'type' : 'date'}))
    description = forms.CharField(widget=forms.Textarea)
    class Meta:
        """Meta definition for IsseuDescriptionform."""

        model = models.IssueDescription
        fields = '__all__'

class UserForm(forms.ModelForm):
    """Form definition for User."""
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    """Form definition for UserProfileInfo."""

    class Meta:
        """Meta definition for UserProfileInfoform."""

        model = models.UserProfileInfo
        fields = ('portfolio_site','profile_pic')
