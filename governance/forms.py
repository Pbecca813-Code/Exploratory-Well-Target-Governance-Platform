from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import User

from .models import (
    WellTarget,
    WellTargetDocument,
    AdministratorAccessRequest,
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
    
    # =====================================================
# ADMINISTRATOR ACCESS REQUEST FORM
# =====================================================

class AdministratorAccessRequestForm(forms.ModelForm):

    confirm_information = forms.BooleanField(
        required=True,
        label="I confirm that the information provided is correct."
    )

    class Meta:

        model = AdministratorAccessRequest

        fields = [

            "first_name",
            "last_name",
            "company_email",
            "employee_id",

            "company",
            "department",
            "job_title",

            "identification_type",
            "identification_document",
            "profile_photo",

            "reason",

     ]

        widgets = {

            "first_name": forms.TextInput(attrs={
                "placeholder": "First Name"
            }),

            "last_name": forms.TextInput(attrs={
                "placeholder": "Last Name"
            }),

            "company_email": forms.EmailInput(attrs={
                "placeholder": "Company Email"
            }),

            "employee_id": forms.TextInput(attrs={
                "placeholder": "Employee ID (Optional)"
            }),

            "company": forms.TextInput(attrs={
                "placeholder": "Company"
            }),

            "department": forms.TextInput(attrs={
                "placeholder": "Department / Business Unit"
            }),

            "job_title": forms.TextInput(attrs={
                "placeholder": "Job Title"
            }),

            "reason": forms.Textarea(attrs={
                "placeholder": "Reason for requesting administrator access...",
                "rows": 4,
            }),

            "identification_type": forms.Select(attrs={
                "class": "form-control"
            }),

            "identification_document": forms.FileInput(attrs={
                "id": "id_identification_document",
                "class": "upload-input"
            }),

            "profile_photo": forms.FileInput(attrs={
                "id": "id_profile_photo",
               "class": "upload-input"
            }),

        }