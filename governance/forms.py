from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import User

from .models import (
    WellTarget,
    WellTargetDocument,
    AdministratorAccessRequest,
    Project,
    ProjectTeam,
    Company,
    SeismicReview,
    Validation,
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
    
# =====================================================
# EMPLOYEE CREATE FORM
# =====================================================

class EmployeeCreateForm(forms.ModelForm):

    # -----------------------------
    # USER FIELDS
    # -----------------------------

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    # -----------------------------
    # EMPLOYEE PROFILE
    # -----------------------------

    employee_number = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    profile_photo = forms.ImageField(
        required=False
    )

    mobile_number = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    office_location = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    workspace = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    company = forms.ModelChoiceField(
        queryset=Company.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"})
    )

    business_unit = forms.ModelChoiceField(
        queryset=BusinessUnit.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"})
    )

    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"})
    )

    country = forms.ModelChoiceField(
        queryset=Country.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"})
    )

    region = forms.ModelChoiceField(
        queryset=Region.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"})
    )

    basin = forms.ModelChoiceField(
        queryset=Basin.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"})
    )

    job_title = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    role = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    mfa_enabled = forms.BooleanField(
        required=False
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

        validate_password(password)

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
# PROJECT TEAM FORM
# =====================================================

class ProjectTeamForm(forms.ModelForm):

    class Meta:

        model = ProjectTeam

        fields = [

            "employee",

            "role",

        ]

        widgets = {

            "employee": forms.Select(

                attrs={

                    "class": "form-select",

                }

            ),

            "role": forms.Select(

                attrs={

                    "class": "form-select",

                }

            ),

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

# =====================================================
# REVIEW FORM
# =====================================================

class ReviewForm(forms.ModelForm):

    class Meta:

        model = SeismicReview

        fields = [

            "well_target",

            "reviewer",

            "status",

            "remarks",

        ]

        widgets = {

            "well_target": forms.Select(attrs={
                "class": "form-select"
            }),

            "reviewer": forms.Select(attrs={
                "class": "form-select"
            }),

            "status": forms.Select(attrs={
                "class": "form-select"
            }),

            "remarks": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
            }),

        }

        # =====================================================
# VALIDATION FORM
# =====================================================

class ValidationForm(forms.ModelForm):

    class Meta:

        model = Validation

        fields = [

            "well_target",

            "validator",

            "status",

            "remarks",

        ]

        widgets = {

            "well_target": forms.Select(attrs={
                "class": "form-select"
            }),

            "validator": forms.Select(attrs={
                "class": "form-select"
            }),

            "status": forms.Select(attrs={
                "class": "form-select"
            }),

            "remarks": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
            }),

        }

# =====================================================
# EMPLOYEE EDIT FORM
# =====================================================

class EmployeeEditForm(forms.ModelForm):

    class Meta:

        model = User

        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
        ]

        widgets = {

            "first_name": forms.TextInput(attrs={
                "class": "form-control",
            }),

            "last_name": forms.TextInput(attrs={
                "class": "form-control",
            }),

            "username": forms.TextInput(attrs={
                "class": "form-control",
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
            }),

        }