from django.urls import path
from .views import imprimer_acte

app_name = "documents"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("dashboard.urls")),
    path("naissances/", include("naissances.urls")),
    path("mariages/", include("mariages.urls")),
    path("deces/", include("deces.urls")),
    path("recherche/", include("recherches.urls")),
    path("documents/", include("documents.urls")),
]