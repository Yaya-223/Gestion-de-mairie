from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render

from etat_civil.models import Acte

@login_required
def imprimer_acte(request, acte_id):
    acte = Acte.objects.filter(
        id=acte_id,
        mairie=request.user.mairie
    ).first()

    if not acte:
        raise Http404("Acte introuvable.")

    return render(
        request,
        "documents/acte_impression.html",
        {"acte": acte},
    )