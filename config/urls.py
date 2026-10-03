from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("dashboard.urls")),

    path(
        "naissances/",
        include("naissances.urls"),
    ),

    path(
        "mariages/",
        include("mariages.urls"),
    ),

    path(
        "deces/",
        include("deces.urls"),
    ),

    path(
        "recherche/",
        include("recherches.urls"),
    ),
]