from .models import BlogModel

from django import forms

class BlogForm(forms.ModelForm):
    class Meta:
        model= BlogModel
        fields = ['title','desc']

        labels ={
            'title':'Enter Your Title ',
            'desc':'Enter Your Description '
        }

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.Textarea(attrs={'class':'form-control'})
        }