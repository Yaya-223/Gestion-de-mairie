from django.urls import path

from .views import valider_acte

app_name = "etat_civil"

urlpatterns = [
path(
        "acte/<uuid:acte_id>/valider/",
        valider_acte,
        name="valider_acte",
    ),
    
path("etat-civil/", include("etat_civil.urls")),
]