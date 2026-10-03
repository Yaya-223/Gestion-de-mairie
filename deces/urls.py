from django.urls import path
from .views import creer_deces

app_name = "deces"

urlpatterns = [
    path("nouveau/", creer_deces, name="creer"),
]