from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import User

from .models import (
    WellTarget,
    WellTargetDocument,
)


class WellTargetForm(forms.ModelForm):

    class Meta:
        model = WellTarget

        fields = [
            "target_name",
            "basin",
            "status",
        ]


class WellTargetDocumentForm(forms.ModelForm):

    class Meta:
        model = WellTargetDocument

        fields = [
            "well_target",
            "file",
        ]


class RegisterUserForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User

        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        ]

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")

        if password != confirm:
            raise forms.ValidationError(
                "Passwords do not match."
            )

        return cleaned_data

    def clean_password(self):

        password = self.cleaned_data.get("password")

        validate_password(password)

        return password
    
class EmployeeCreateForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput()
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:

        model = User

        fields = [

            "first_name",

            "last_name",

            "username",

            "email",

        ]

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get("password")

        confirm = cleaned_data.get("confirm_password")

        if password != confirm:

            raise forms.ValidationError(
                "Passwords do not match."
            )

        return cleaned_data