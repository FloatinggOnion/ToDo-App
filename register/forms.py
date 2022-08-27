from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)


    class Meta:
        model = User #We're changing the user model everytime we save something to this form
        fields = ('username', 'email', 'password1', 'password2') #This specifies the fields we want in the form. If you are adding others, you can put them in. This is in order of preference

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user