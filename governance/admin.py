from django.contrib import admin

from .models import (
    WellTarget,
    WellTargetDocument,
    SeismicReview,
    Validation,
    TargetApproval,
    WellTargetHistory
)

admin.site.register(WellTarget)
admin.site.register(WellTargetDocument)
admin.site.register(SeismicReview)
admin.site.register(Validation)
admin.site.register(TargetApproval)
admin.site.register(WellTargetHistory)

admin.site.site_header = "Administrator"

admin.site.site_title = "Administrator"

admin.site.index_title = "System Administration"

from .models import AdministratorAccessRequest


@admin.register(AdministratorAccessRequest)
class AdministratorAccessRequestAdmin(admin.ModelAdmin):

    list_display = (
        "first_name",
        "last_name",
        "company_email",
        "company",
        "department",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "company",
    )

    search_fields = (
        "first_name",
        "last_name",
        "company_email",
    )

    ordering = (
        "-created_at",
    )