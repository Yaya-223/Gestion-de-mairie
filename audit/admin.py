from django.contrib import admin
from .models import JournalAudit


@admin.register(JournalAudit)
class JournalAuditAdmin(admin.ModelAdmin):
    list_display = (
        "date_action",
        "utilisateur",
        "mairie",
        "action",
        "objet",
        "adresse_ip",
    )

    list_filter = (
        "action",
        "mairie",
        "date_action",
    )

    search_fields = (
        "utilisateur__username",
        "action",
        "objet",
        "adresse_ip",
    )

    readonly_fields = (
        "utilisateur",
        "mairie",
        "action",
        "objet",
        "adresse_ip",
        "date_action",
    )