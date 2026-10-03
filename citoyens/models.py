import uuid

from django.db import models


class Citoyen(models.Model):
    class Sexe(models.TextChoices):
        MASCULIN = "M", "Masculin"
        FEMININ = "F", "Féminin"

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    mairie = models.ForeignKey(
        "mairie.Mairie",
        on_delete=models.PROTECT,
        related_name="citoyens",
    )

    nom = models.CharField(
        max_length=100,
    )

    prenom = models.CharField(
        max_length=150,
    )

    sexe = models.CharField(
        max_length=1,
        choices=Sexe.choices,
    )

    date_naissance = models.DateField(
        null=True,
        blank=True,
    )

    lieu_naissance = models.CharField(
        max_length=200,
        blank=True,
    )

    nationalite = models.CharField(
        max_length=100,
        default="Malienne",
    )

    profession = models.CharField(
        max_length=150,
        blank=True,
    )

    adresse = models.TextField(
        blank=True,
    )

    telephone = models.CharField(
        max_length=30,
        blank=True,
    )

    email = models.EmailField(
        blank=True,
    )

    numero_piece_identite = models.CharField(
        max_length=100,
        blank=True,
    )

    date_creation = models.DateTimeField(
        auto_now_add=True,
    )

    date_modification = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = "Citoyen"
        verbose_name_plural = "Citoyens"
        ordering = ["nom", "prenom"]
        indexes = [
            models.Index(fields=["nom", "prenom"]),
            models.Index(fields=["date_naissance"]),
            models.Index(fields=["numero_piece_identite"]),
        ]

    def __str__(self):
        return f"{self.nom} {self.prenom}"