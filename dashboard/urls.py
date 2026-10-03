from django.urls import path
from .views import accueil

app_name = "dashboard"

urlpatterns = [
    path("", accueil, name="accueil"),
]