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
from high_level import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("Facture/<int:pk>", views.FactureDetailView.as_view(), name="Facture"),
    path(
        "Fournisseur/<int:pk>",
        views.FournisseurDetailView.as_view(),
        name="Fournisseur",
    ),
    path("Lieu/<int:pk>", views.LieuDetailView.as_view(), name="facture"),
    path("Machine/<int:pk>", views.MachineDetailView.as_view(), name="Machine"),
    path(
        "Operation/<int:pk>",
        views.OperationDetailView.as_view(),
        name="Operation",
    ),
    path("Pays/<int:pk>", views.PaysDetailView.as_view(), name="Pays"),
    path(
        "PointDeVente/<int:pk>",
        views.PointDeVenteDetailView.as_view(),
        name="PointDeVente",
    ),
    path(
        "PrixProduit/<int:pk>",
        views.PrixProduitDetailView.as_view(),
        name="PrixProduit",
    ),
    path("Produit/<int:pk>", views.ProduitDetailView.as_view(), name="Produit"),
    path(
        "QuantiteMachine/<int:pk>",
        views.QuantiteMachineDetailView.as_view(),
        name="QuantiteMachine",
    ),
    path(
        "QuantiteProduit/<int:pk>",
        views.QuantiteProduitDetailView.as_view(),
        name="QuantiteProduit",
    ),
    path("Stock/<int:pk>", views.StockDetailView.as_view(), name="Stock"),
    path(
        "Transport/<int:pk>",
        views.TransportDetailView.as_view(),
        name="Transport",
    ),
    path("Ville/<int:pk>", views.VilleDetailView.as_view(), name="Ville"),
]
