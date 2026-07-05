from django import forms
from .models import WellTarget, WellTargetDocument


class WellTargetForm(forms.ModelForm):

    class Meta:

        model = WellTarget

        fields = [
            'target_name',
            'basin',
            'status'
        ]
class WellTargetDocumentForm(forms.ModelForm):

    class Meta:

        model = WellTargetDocument

        fields = [
            'well_target',
            'file'
        ]