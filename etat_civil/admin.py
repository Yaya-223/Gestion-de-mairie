from django.contrib import admin
from .models import Acte


@admin.register(Acte)
class ActeAdmin(admin.ModelAdmin):
    list_display = (
        "numero",
        "type_acte",
        "mairie",
        "annee",
        "date_acte",
        "statut",
        "cree_par",
        "valide_par",
        "date_creation",
    )

    list_filter = (
        "type_acte",
        "statut",
        "annee",
        "mairie",
    )

    search_fields = (
        "numero",
        "observation",
    )

    readonly_fields = (
        "date_creation",
        "date_modification",
    )