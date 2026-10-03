from django.contrib import admin

from .models import Citoyen


@admin.register(Citoyen)
class CitoyenAdmin(admin.ModelAdmin):
    list_display = (
        "nom",
        "prenom",
        "sexe",
        "date_naissance",
        "lieu_naissance",
        "mairie",
        "telephone",
    )

    search_fields = (
        "nom",
        "prenom",
        "numero_piece_identite",
        "telephone",
    )

    list_filter = (
        "sexe",
        "mairie",
        "nationalite",
    )

    autocomplete_fields = (
        "mairie",
    )

    ordering = (
        "nom",
        "prenom",
    )