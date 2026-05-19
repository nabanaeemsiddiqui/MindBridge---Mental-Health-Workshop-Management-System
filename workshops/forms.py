from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class CustomUserForm(UserCreationForm):

    email = forms.EmailField(required=True)
    
    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():

            field.widget.attrs.update({
                'class': 'form-control'
            })

    def clean_username(self):

        username = self.cleaned_data['username']

        if User.objects.filter(username=username).exists():

            raise ValidationError(
                "This username is already taken."
            )

        return username
    
    