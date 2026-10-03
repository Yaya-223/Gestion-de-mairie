from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from citoyens.models import Citoyen
from etat_civil.models import Acte
from naissances.models import Naissance
from mariages.models import Mariage
from deces.models import Deces


@login_required
def accueil(request):

    mairie = request.user.mairie

    citoyens = Citoyen.objects.filter(mairie=mairie).count()
    actes = Acte.objects.filter(mairie=mairie).count()
    naissances = Naissance.objects.filter(
        acte__mairie=mairie
    ).count()
    mariages = Mariage.objects.filter(
        acte__mairie=mairie
    ).count()
    deces = Deces.objects.filter(
        acte__mairie=mairie
    ).count()

    return render(
        request,
        "dashboard/accueil.html",
        {
            "mairie": mairie,
            "citoyens": citoyens,
            "actes": actes,
            "naissances": naissances,
            "mariages": mariages,
            "deces": deces,
        },
    )