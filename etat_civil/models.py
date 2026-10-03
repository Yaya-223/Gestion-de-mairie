import uuid

from django.conf import settings
from django.db import models


class Acte(models.Model):
    class TypeActe(models.TextChoices):
        NAISSANCE = "NAISSANCE", "Naissance"
        MARIAGE = "MARIAGE", "Mariage"
        DECES = "DECES", "Décès"

    class Statut(models.TextChoices):
        BROUILLON = "BROUILLON", "Brouillon"
        VALIDE = "VALIDE", "Validé"
        ANNULE = "ANNULE", "Annulé"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    mairie = models.ForeignKey(
        "mairie.Mairie",
        on_delete=models.PROTECT,
        related_name="actes",
    )

    numero = models.CharField(
        max_length=50,
    )

    type_acte = models.CharField(
        max_length=20,
        choices=TypeActe.choices,
    )

    annee = models.PositiveIntegerField()

    date_acte = models.DateField()

    statut = models.CharField(
        max_length=20,
        choices=Statut.choices,
        default=Statut.BROUILLON,
    )

    observation = models.TextField(
        blank=True,
    )

    cree_par = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="actes_crees",
    )

    valide_par = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="actes_valides",
        null=True,
        blank=True,
    )

    date_creation = models.DateTimeField(
        auto_now_add=True,
    )

    date_modification = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = "Acte"
        verbose_name_plural = "Actes"
        ordering = ["-date_acte", "-date_creation"]
        constraints = [
            models.UniqueConstraint(
                fields=["mairie", "numero"],
                name="unique_numero_acte_par_mairie",
            ),
        ]
        indexes = [
            models.Index(fields=["mairie", "type_acte"]),
            models.Index(fields=["mairie", "annee"]),
            models.Index(fields=["numero"]),
            models.Index(fields=["date_acte"]),
        ]

    def __str__(self):
        return f"{self.numero} - {self.get_type_acte_display()}"