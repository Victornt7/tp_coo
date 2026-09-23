from django.db import models


class Pays(models.Model):
    nom = models.CharField(max_length=48)
    tva = models.FloatField()
    tarif_electrique = models.FloatField()
    salaire_minimum = models.FloatField()

    def __str__(self):
        return self.nom


class Ville(models.Model):
    nom = models.CharField(max_length=58)
    taxe_immobiliere = models.FloatField()
    prix_m2 = models.FloatField()
    pays = models.ForeignKey(Pays, on_delete=models.PROTECT)

    def __str__(self):
        return self.nom


class Machine(models.Model):
    nom = models.CharField(max_length=50)
    prix = models.FloatField()
    duree_de_vie = models.FloatField()
    cout_maintenance = models.FloatField()
    superficie = models.FloatField()

    def __str__(self):
        return self.nom


class QuantiteMachine(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
    nombre = models.IntegerField()

    def __str__(self):
        return f"{self.machine.nom} x {self.nombre}"


class Lieu(models.Model):
    nom = models.CharField(max_length=50)
    ville = models.ForeignKey(Ville, on_delete=models.PROTECT)
    superficie = models.FloatField()
    quantite_machines = models.ManyToManyField(Machine)
    consommation_electrique = models.FloatField()

    def __str__(self):
        return self.nom


class Transport(models.Model):
    nombre_palettes = models.IntegerField()
    cout = models.FloatField()
    delai = models.FloatField()
    depart = models.ForeignKey(Lieu, on_delete=models.PROTECT, related_name="depart")
    arrivee = models.ForeignKey(Lieu, on_delete=models.PROTECT)

    def __str__(self):
        return self.depart.nom + " to " + self.arrivee.nom


class Operation(models.Model):
    nom = models.CharField(max_length=50)
    operation_suivante = models.ForeignKey("self", on_delete=models.PROTECT)
    cout = models.FloatField()
    machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
    quantite_produits = models.ForeignKey("QuantiteProduit", on_delete=models.PROTECT)
    heures_de_travail = models.FloatField()
    consomation_electrique = models.FloatField()

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=50)
    prix_de_vente = models.FloatField()
    duree_de_vie = models.FloatField()
    nombre_par_palette = models.IntegerField()
    operations = models.ForeignKey(Operation, on_delete=models.PROTECT)

    def __str__(self):
        return self.nom


class PrixProduit(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.PROTECT)
    prix_achat = models.FloatField()

    def __str__(self):
        return f"{self.produit}: {self.prix_achat}"


class Fournisseur(models.Model):
    nom = models.CharField(max_length=50)
    prix_produit = models.ForeignKey(PrixProduit, on_delete=models.PROTECT)

    def __str__(self):
        return self.nom


class QuantiteProduit(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.PROTECT)
    nombre = models.IntegerField()

    def __str__(self):
        return f"{self.produit} x {self.nombre}"


class Stock(models.Model):
    quantite_produit = models.ForeignKey(QuantiteProduit, on_delete=models.PROTECT)
    palettes_max = models.IntegerField()

    def __str__(self):
        return f"{self.quantite_produit}, palettes max: {self.palettes_max}"


class PointDeVente(models.Model):
    nom = models.CharField(max_length=50)
    lieu = models.ForeignKey(Lieu, on_delete=models.PROTECT)
    heures_de_travail = models.FloatField()
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT)

    def __str__(self):
        return self.nom


class Facture(models.Model):
    quantite_produit = models.ManyToManyField(QuantiteProduit)
    reduction = models.FloatField()
    point_de_vente = models.ForeignKey(PointDeVente, on_delete=models.PROTECT)
    client = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.quantite_produit}, reduction: {self.reduction}, à {self.point_de_vente} pour {self.client}"
