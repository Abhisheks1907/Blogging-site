from django import forms
from django.contrib.auth.models import User
from .models import user_Profile



class userProfileForm(forms.ModelForm):
    class Meta:
        model = user_Profile
        fields = ['img','about']

