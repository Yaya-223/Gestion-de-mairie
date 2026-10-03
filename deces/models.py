from django.db import models


class Deces(models.Model):
    acte = models.OneToOneField(
        "etat_civil.Acte",
        on_delete=models.PROTECT,
        related_name="deces",
    )

    defunt = models.ForeignKey(
        "citoyens.Citoyen",
        on_delete=models.PROTECT,
        related_name="deces",
    )

    date_deces = models.DateField()

    heure_deces = models.TimeField(
        null=True,
        blank=True,
    )

    lieu_deces = models.CharField(
        max_length=200,
    )

    cause_deces = models.CharField(
        max_length=250,
        blank=True,
    )

    declarant_nom = models.CharField(
        max_length=200,
        blank=True,
    )

    declarant_qualite = models.CharField(
        max_length=150,
        blank=True,
    )

    observations = models.TextField(
        blank=True,
    )

    class Meta:
        verbose_name = "Acte de décès"
        verbose_name_plural = "Actes de décès"

    def __str__(self):
        return f"Décès - {self.defunt}"