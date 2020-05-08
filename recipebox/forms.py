from django import forms
from recipebox.models import Author
from django.contrib.auth.models import User


class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)
    user = forms.ModelChoiceField(queryset=User.objects.all())
    # exclude = ["user"]


class AddRecipeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super(AddRecipeForm, self).__init__(*args, **kwargs)
        if user.is_staff:
            self.fields["author"].queryset = Author.objects.all()
        else:
            self.fields["author"].queryset = Author.objects.filter(user=user)

    title = forms.CharField(max_length=50)
    author = forms.ModelChoiceField(queryset=None)
    description = forms.CharField(max_length=140)
    time_req = forms.CharField(max_length=25)
    instructions = forms.CharField(widget=forms.Textarea)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
