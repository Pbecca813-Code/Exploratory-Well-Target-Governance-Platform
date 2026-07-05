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