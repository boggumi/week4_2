from django import forms
from blogapp.models import Blog

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']


class BlogPost(forms.ModelForm):
    email = forms.EmailField()
    url = forms.URLField()
    files = forms.FieldField()
    words = forms.CharField(max_length=200)
    max_number = forms.ChoiceField(choice=[('1','one'),('2','two'),('3','three')])