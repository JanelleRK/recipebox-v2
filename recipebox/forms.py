from django import forms
from recipebox.models import Author


class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(max_length=140)
    time_req = forms.CharField(max_length=25)
    instructions = forms.CharField(widget=forms.Textarea)
