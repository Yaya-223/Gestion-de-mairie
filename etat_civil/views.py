from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.core.exceptions import PermissionDenied

from .models import Acte
from audit.models import JournalAudit


@login_required
def valider_acte(request, acte_id):
    acte = get_object_or_404(
        Acte,
        id=acte_id,
        mairie=request.user.mairie,
    )

    if acte.statut == Acte.Statut.BROUILLON:
        acte.statut = Acte.Statut.VALIDE
        acte.valide_par = request.user
        acte.save()

        messages.success(
            request,
            f"L'acte {acte.numero} a été validé avec succès."
        )

    return redirect("documents:imprimer_acte", acte_id=acte.id)

JournalAudit.objects.create(
    utilisateur=request.user,
    mairie=request.user.mairie,
    action="VALIDATION_ACTE",
    objet=acte.numero,
    adresse_ip=request.META.get("REMOTE_ADDR"),
)