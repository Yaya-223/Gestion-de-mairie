from django import forms
from .models import Deces


class DecesForm(forms.ModelForm):
    class Meta:
        model = Deces
        fields = [
            "defunt",
            "date_deces",
            "heure_deces",
            "lieu_deces",
            "cause_deces",
            "declarant_nom",
            "declarant_qualite",
            "observations",
        ]

        widgets = {
            "date_deces": forms.DateInput(
                attrs={"type": "date"}
            ),
            "heure_deces": forms.TimeInput(
                format="%H:%M",
                attrs={"type": "time"}
            ),
            "observations": forms.Textarea(
                attrs={"rows": 4}
            ),
        }