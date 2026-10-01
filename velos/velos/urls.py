"""
URL configuration for velos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from velos.high_level.models import (
    Facture,
    Fournisseur,
    Lieu,
    Machine,
    Operation,
    Pays,
    PointDeVente,
    PrixProduit,
    Produit,
    QuantiteMachine,
    QuantiteProduit,
    Stock,
    Transport,
    Ville,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "Facture/int<int:pk>", Facture.views.FactureDetailView.as_view(), name="Facture"
    ),
    path(
        "Fournisseur/int<int:pk>",
        Fournisseur.views.FactureDetailView.as_view(),
        name="Fournisseur",
    ),
    path("Lieu/int<int:pk>", Lieu.views.FactureDetailView.as_view(), name="facture"),
    path(
        "Machine/int<int:pk>", Machine.views.FactureDetailView.as_view(), name="Machine"
    ),
    path(
        "Operation/int<int:pk>",
        Operation.views.FactureDetailView.as_view(),
        name="Operation",
    ),
    path("Pays/int<int:pk>", Pays.views.FactureDetailView.as_view(), name="Pays"),
    path(
        "PointDeVente/int<int:pk>",
        PointDeVente.views.FactureDetailView.as_view(),
        name="PointDeVente",
    ),
    path(
        "PrixProduit/int<int:pk>",
        PrixProduit.views.FactureDetailView.as_view(),
        name="PrixProduit",
    ),
    path(
        "Produit/int<int:pk>", Produit.views.FactureDetailView.as_view(), name="Produit"
    ),
    path(
        "QuantiteMachine/int<int:pk>",
        QuantiteMachine.views.FactureDetailView.as_view(),
        name="QuantiteMachine",
    ),
    path(
        "QuantiteProduit/int<int:pk>",
        QuantiteProduit.views.FactureDetailView.as_view(),
        name="QuantiteProduit",
    ),
    path("Stock/int<int:pk>", Stock.views.FactureDetailView.as_view(), name="Stock"),
    path(
        "Transport/int<int:pk>",
        Transport.views.FactureDetailView.as_view(),
        name="Transport",
    ),
    path("Ville/int<int:pk>", Ville.views.FactureDetailView.as_view(), name="Ville"),
]
