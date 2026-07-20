from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import User

from .models import (
    WellTarget,
    WellTargetDocument,
    AdministratorAccessRequest,
    Project,
    Company,
    Department,
    BusinessUnit,
    Country,
    Region,
    Basin,
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

    # Personal Information
    "first_name",
    "last_name",
    "company_email",
    "mobile_number",
    "home_address",
    "employee_id",

    # Organization Information
    "company",
    "department",
    "job_title",
    "company_phone",
    "company_address",
    "office_location",

    # Identity Verification
    "identification_type",
    "identification_document",
    "profile_photo",

    # Request
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

            "mobile_number": forms.TextInput(attrs={
            "placeholder": "Mobile Number"
           }),

            "home_address": forms.TextInput(attrs={
            "placeholder": "Home Address"
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

            "company_phone": forms.TextInput(attrs={
            "placeholder": "Company Phone"
            }),

            "company_address": forms.TextInput(attrs={
            "placeholder": "Company Address"
            }),

           "office_location": forms.TextInput(attrs={
           "placeholder": "Office Location"
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

        # =====================================================
# PROJECT FORM
# =====================================================

class ProjectForm(forms.ModelForm):

    class Meta:

        model = Project

        fields = [

            "project_name",

            "description",

            "lead_interpreter",

            "status",

            "start_date",

            "end_date",

        ]

        widgets = {

            "project_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Project Name"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Project Description"
            }),

            "lead_interpreter": forms.Select(attrs={
                "class": "form-select"
            }),

            "status": forms.Select(attrs={
                "class": "form-select"
            }),

            "start_date": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control"
            }),

            "end_date": forms.DateInput(attrs={
                "type": "date",
                "class": "form-control"
            }),

        }

        # =====================================================
# COMPANY FORM
# =====================================================

class CompanyForm(forms.ModelForm):

    class Meta:

        model = Company

        fields = [
            "name",
            "is_active",
        ]

        widgets = {

            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Company Name"
            }),

            "is_active": forms.CheckboxInput(attrs={
                "class": "form-check-input"
            }),

        }