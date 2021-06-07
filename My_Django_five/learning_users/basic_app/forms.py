from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo
from django.core import validators


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    


    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        #crf hidden for security ex to ensure input dont going to another website
        botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])


                             

#form
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')