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
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected')
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
        choices=REVIEW_STATUS
    )

    review_date = models.DateTimeField(
        auto_now_add=True
    )

    remarks = models.TextField()

    def __str__(self):
        return f"Review - {self.well_target}"    
class Validation(models.Model):

    VALIDATION_STATUS = [
        ('VALID', 'Valid'),
        ('INVALID', 'Invalid')
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