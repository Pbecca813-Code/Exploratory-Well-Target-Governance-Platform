from django.db import models
from django.contrib.auth.models import User


class WellTarget(models.Model):

    STATUS_CHOICES = [
        ('DRAFT', 'Draft'),
        ('UNDER_REVIEW', 'Under Review'),
        ('VALIDATED', 'Validated'),
        ('PENDING_APPROVAL', 'Pending Approval'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    target_name = models.CharField(max_length=200)

    project = models.ForeignKey(
    "Project",
    on_delete=models.CASCADE,
    related_name="well_targets",
    null=True,
    blank=True
   )

    basin = models.CharField(max_length=100)

    lead_interpreter = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='DRAFT'
    )

    created_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.target_name
class WellTargetDocument(models.Model):

    well_target = models.ForeignKey(
        WellTarget,
        on_delete=models.CASCADE
    )

    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    file = models.FileField(
        upload_to='documents/'
    )

    upload_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.file.name
class SeismicReview(models.Model):

    REVIEW_STATUS = [

        ("PENDING", "Pending"),

        ("IN_PROGRESS", "In Progress"),

        ("COMPLETED", "Completed"),

    ]

    well_target = models.ForeignKey(
        WellTarget,
        on_delete=models.CASCADE
    )

    reviewer = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    status = models.CharField(

        max_length=20,

        choices=REVIEW_STATUS,

        default="PENDING"

    )

    review_date = models.DateTimeField(
        auto_now_add=True
    )

    remarks = models.TextField()

    def __str__(self):
        return f"Review - {self.well_target}"   
     
class Validation(models.Model):

    VALIDATION_STATUS = [

        ("PENDING", "Pending"),

        ("IN_PROGRESS", "In Progress"),

        ("COMPLETED", "Completed"),

    ]

    well_target = models.ForeignKey(
        WellTarget,
        on_delete=models.CASCADE
    )

    validator = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=VALIDATION_STATUS
    )

    validation_date = models.DateTimeField(
        auto_now_add=True
    )

    remarks = models.TextField()

    def __str__(self):
        return f"Validation - {self.well_target}"
    
class TargetApproval(models.Model):

    APPROVAL_STATUS = [
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected')
    ]

    well_target = models.ForeignKey(
        WellTarget,
        on_delete=models.CASCADE
    )

    approver = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=APPROVAL_STATUS
    )

    approval_date = models.DateTimeField(
        auto_now_add=True
    )

    remarks = models.TextField()

    def __str__(self):
        return f"Approval - {self.well_target}"
class WellTargetHistory(models.Model):

    well_target = models.ForeignKey(
        WellTarget,
        on_delete=models.CASCADE
    )

    performed_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    action = models.CharField(
        max_length=200
    )

    remarks = models.TextField()

    action_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.action
    
# =====================================================
# ADMINISTRATOR ACCESS REQUEST
# =====================================================

class AdministratorAccessRequest(models.Model):

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
    ]

    IDENTIFICATION_CHOICES = [
        ("COMPANY_BADGE", "Company ID Badge"),
        ("NATIONAL_ID", "National ID Card"),
        ("PASSPORT", "Passport"),
        ("DRIVERS_LICENSE", "Driver's License"),
        ("OTHER", "Other"),
    ]

    # =====================================================
    # PERSONAL INFORMATION
    # =====================================================

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    company_email = models.EmailField()

    mobile_number = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    home_address = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    employee_id = models.CharField(
        max_length=50,
        blank=True
    )

    # =====================================================
    # ORGANIZATION INFORMATION
    # =====================================================

    company = models.CharField(
        max_length=150
    )

    department = models.CharField(
        max_length=150
    )

    job_title = models.CharField(
        max_length=150
    )

    company_phone = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    company_address = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    office_location = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )

    # =====================================================
    # IDENTITY VERIFICATION
    # =====================================================

    identification_type = models.CharField(
        max_length=30,
        choices=IDENTIFICATION_CHOICES,
        blank=True
    )

    identification_document = models.FileField(
        upload_to="uploads/admin_requests/documents/",
        blank=True,
        null=True
   )

    profile_photo = models.ImageField(
        upload_to="uploads/admin_requests/photos/",
        blank=True,
        null=True
    )

    # =====================================================
    # REQUEST INFORMATION
    # =====================================================

    reason = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    review_comments = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    reviewed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):

        return f"{self.first_name} {self.last_name} ({self.status})"
    
# =====================================================
# PROJECT
# =====================================================

class Project(models.Model):

    PROJECT_STATUS = [
        ("PLANNING", "Planning"),
        ("ACTIVE", "Active"),
        ("ON_HOLD", "On Hold"),
        ("COMPLETED", "Completed"),
        ("ARCHIVED", "Archived"),
    ]

    project_name = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True
    )

    lead_interpreter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="led_projects"
    )

    status = models.CharField(
        max_length=20,
        choices=PROJECT_STATUS,
        default="PLANNING"
    )

    start_date = models.DateField(
        null=True,
        blank=True
    )

    end_date = models.DateField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.project_name
    
# =====================================================
# PROJECT TEAM
# =====================================================

class ProjectTeam(models.Model):

    ROLE_CHOICES = [

        ("PROJECT_MANAGER", "Project Manager"),

        ("LEAD_INTERPRETER", "Lead Interpreter"),

        ("REVIEWER", "Reviewer"),

        ("VALIDATOR", "Validator"),

        ("APPROVER", "Approver"),

        ("TEAM_MEMBER", "Team Member"),

    ]

    project = models.ForeignKey(

        Project,

        on_delete=models.CASCADE,

        related_name="team_members"

    )

    employee = models.ForeignKey(

        User,

        on_delete=models.CASCADE,

        related_name="project_assignments"

    )

    role = models.CharField(

        max_length=30,

        choices=ROLE_CHOICES

    )

    assigned_by = models.ForeignKey(

        User,

        on_delete=models.SET_NULL,

        null=True,

        blank=True,

        related_name="assigned_projects"

    )

    assigned_date = models.DateTimeField(

        auto_now_add=True

    )

    class Meta:

        unique_together = ("project", "employee")

    def __str__(self):

        return f"{self.employee} - {self.project}"

    # =====================================================
# PROJECT MEMBER
# =====================================================

class ProjectMember(models.Model):

    PROJECT_ROLE = [
        ("LEAD_INTERPRETER", "Lead Interpreter"),
        ("SENIOR_INTERPRETER", "Senior Interpreter"),
        ("INTERPRETER", "Interpreter"),
        ("REVIEWER", "Reviewer"),
        ("VALIDATOR", "Validator"),
        ("APPROVER", "Approver"),
        ("VIEWER", "Viewer"),
    ]

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="members"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="project_memberships"
    )

    role = models.CharField(
        max_length=30,
        choices=PROJECT_ROLE
    )

    assigned_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="assigned_project_members"
    )

    assigned_date = models.DateTimeField(
        auto_now_add=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        unique_together = ("project", "user")

    def __str__(self):
        return f"{self.user.username} - {self.project.project_name}"
    
    # =====================================================
# COMPANY
# =====================================================

class Company(models.Model):

    name = models.CharField(
        max_length=150,
        unique=True
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name
    
    # =====================================================
# DEPARTMENT
# =====================================================

class Department(models.Model):

    name = models.CharField(
        max_length=150,
        unique=True
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name
    
    # =====================================================
# BUSINESS UNIT
# =====================================================

class BusinessUnit(models.Model):

    name = models.CharField(
        max_length=150,
        unique=True
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name
    
    # =====================================================
# COUNTRY
# =====================================================

class Country(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name
    
    # =====================================================
# REGION
# =====================================================

class Region(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name="regions"
    )

    def __str__(self):
        return self.name
    
    # =====================================================
# BASIN
# =====================================================

class Basin(models.Model):

    name = models.CharField(
        max_length=150,
        unique=True
    )

    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name="basins"
    )

    def __str__(self):
        return self.name

# =====================================================
# EMPLOYEE PROFILE
# =====================================================

class EmployeeProfile(models.Model):

    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive"),
        ("ON_LEAVE", "On Leave"),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    employee_number = models.CharField(
        max_length=20,
        unique=True
    )

    profile_photo = models.ImageField(
        upload_to="employees/",
        blank=True,
        null=True
    )

    mobile_number = models.CharField(
        max_length=30,
        blank=True
    )

    office_location = models.CharField(
        max_length=100,
        blank=True
    )

    workspace = models.CharField(
        max_length=100,
        blank=True
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    business_unit = models.ForeignKey(
        BusinessUnit,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    region = models.ForeignKey(
        Region,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    basin = models.ForeignKey(
        Basin,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    job_title = models.CharField(
        max_length=100,
        blank=True
    )

    role = models.CharField(
        max_length=100,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ACTIVE"
    )

    mfa_enabled = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.employee_number} - {self.user.get_full_name()}"