from django import forms
from .models import Post

class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["description","url","tags"]
        labels={
            "description":"Caption",
            "tags":"Category"
        }
        widgets={
            "description":forms.Textarea(attrs={"rows":3,"placeholder":"Add a Caption...","class":"font2 text-4xl"}),
            "url":forms.TextInput(attrs={"placeholder":"Add url..."}),
            "tags":forms.CheckboxSelectMultiple(attrs={"id":"id_tags"})
        }
class EditPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["description","tags"]
        labels={
            "description":"",
            "tags":"Category"
        }
        widgets={
            "description":forms.Textarea(attrs={"rows":3,"class":"font2 text-4xl"}),
            "tags":forms.CheckboxSelectMultiple(attrs={"id":"id_tags"})
        }


        