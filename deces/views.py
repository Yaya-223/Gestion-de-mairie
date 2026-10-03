from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import redirect, render

from etat_civil.models import Acte

from .forms import DecesForm
from .models import Deces


def generer_numero_acte(mairie, annee):
    prefixe = f"DEC-{annee}-"

    dernier_acte = (
        Acte.objects
        .filter(
            mairie=mairie,
            type_acte=Acte.TypeActe.DECES,
            annee=annee,
            numero__startswith=prefixe,
        )
        .order_by("-numero")
        .first()
    )

    if dernier_acte:
        dernier_numero = int(dernier_acte.numero.split("-")[-1])
        prochain_numero = dernier_numero + 1
    else:
        prochain_numero = 1

    return f"{prefixe}{prochain_numero:06d}"


@login_required
@transaction.atomic
def creer_deces(request):

    mairie = request.user.mairie

    if not mairie:
        messages.error(
            request,
            "Votre compte utilisateur n'est associé à aucune mairie."
        )
        return redirect("admin:index")

    if request.method == "POST":

        form = DecesForm(request.POST)

        if form.is_valid():

            date_deces = form.cleaned_data["date_deces"]
            annee = date_deces.year

            numero = generer_numero_acte(mairie, annee)

            acte = Acte.objects.create(
                mairie=mairie,
                numero=numero,
                type_acte=Acte.TypeActe.DECES,
                annee=annee,
                date_acte=date_deces,
                statut=Acte.Statut.BROUILLON,
                cree_par=request.user,
            )

            deces = form.save(commit=False)
            deces.acte = acte
            deces.save()

            messages.success(
                request,
                f"Le décès a été enregistré sous le numéro {numero}."
            )

            return redirect("deces:creer")

    else:
        form = DecesForm()

    deces_liste = (
        Deces.objects
        .filter(acte__mairie=mairie)
        .select_related(
            "acte",
            "defunt",
        )
        .order_by("-acte__date_creation")[:30]
    )

    return render(
        request,
        "deces/deces_form.html",
        {
            "form": form,
            "mairie": mairie,
            "deces_liste": deces_liste,
        },
    )