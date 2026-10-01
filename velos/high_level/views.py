from django.http import JsonResponse
from django.views.generic import DetailView

from .models import (
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


class FactureDetailView(DetailView):
    model = Facture

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class FournisseurDetailView(DetailView):
    model = Fournisseur

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class LieuDetailView(DetailView):
    model = Lieu

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class MachineDetailView(DetailView):
    model = Machine

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class OperationDetailView(DetailView):
    model = Operation

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class PaysDetailView(DetailView):
    model = Pays

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class PointDeVenteDetailView(DetailView):
    model = PointDeVente

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class PrixProduitDetailView(DetailView):
    model = PrixProduit

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class ProduitDetailView(DetailView):
    model = Produit

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class QuantiteMachineDetailView(DetailView):
    model = QuantiteMachine

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class QuantiteProduitDetailView(DetailView):
    model = QuantiteProduit

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class StockDetailView(DetailView):
    model = Stock

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class TransportDetailView(DetailView):
    model = Transport

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class VilleDetailView(DetailView):
    model = Ville

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())
