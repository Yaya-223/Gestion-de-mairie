import uuid
from django.conf import settings
from django.db import models


class JournalAudit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    utilisateur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="actions_audit",
    )

    mairie = models.ForeignKey(
        "mairie.Mairie",
        on_delete=models.PROTECT,
        related_name="journaux_audit",
    )

    action = models.CharField(max_length=100)

    objet = models.CharField(max_length=200, blank=True)

    adresse_ip = models.GenericIPAddressField(null=True, blank=True)

    date_action = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Journal d'audit"
        verbose_name_plural = "Journal d'audit"
        ordering = ["-date_action"]

    def __str__(self):
        return f"{self.date_action} - {self.utilisateur} - {self.action}"