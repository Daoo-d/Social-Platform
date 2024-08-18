from django import forms
from .models import Profile

class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
            "image":forms.FileInput(),
            "bio":forms.Textarea(attrs={"rows":3})
        }