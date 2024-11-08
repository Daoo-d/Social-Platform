from django import forms
from .models import Post,Comment,Reply

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

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
        labels={
            "body":""
        }
        widgets = { 
            'body': forms.TextInput(attrs={ 'placeholder': 'Add comment ...'}), 
            }

class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ["body"]
        labels={
            "body":""
        }
        widgets = { 
            'body': forms.TextInput(attrs={ 'placeholder': 'Add reply ...'}), 
            }        


        