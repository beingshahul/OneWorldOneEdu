from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from app.models import Category
# from login.models import Institution

from login.models import Users


class UserForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username')

class MyUserForm(forms.ModelForm):
    interests = forms.ModelMultipleChoiceField( queryset=Category.objects.all() )
    class Meta:
        model = Users
        fields = ('interests',)