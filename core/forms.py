from django import forms
from .models import Post
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "author",
            "tags",
            "imagen_portada",
        ]


class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Contraseña"
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput,
        label="Repetir contraseña"
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
        )

    def clean_password2(self):

        cd = self.cleaned_data

        if cd.get("password") != cd.get("password2"):
            raise forms.ValidationError(
                "Las contraseñas no coinciden"
            )

        return cd.get("password2")