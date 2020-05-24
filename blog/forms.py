from django import forms
from django.forms import TextInput, Textarea
from blog.models import Comment


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('username', 'email', 'body')       
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),
            'body': Textarea(attrs={'class': 'form-control', 'rows': 4})
        }