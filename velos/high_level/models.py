from django.db import models


class Pays(models.Model):
    nom = models.CharField(max_length=48)
    tva = models.FloatField()
    tarif_electrique = models.FloatField()  # en kwh
    salaire_minimum = (
        models.FloatField()
    )  # charges patronales etc comprises donc en gros SMIC x 2

    def __str__(self):
        return self.nom

    def json(self):
        return {
            "nom": self.nom,
            "tva": self.tva,
            "tarif_electrique": self.tarif_electrique,
            "salaire_minimum": self.salaire_minimum,
        }


class Ville(models.Model):
    nom = models.CharField(max_length=58)
    taxe_immobiliere = models.FloatField()
    prix_m2 = models.FloatField()
    pays = models.ForeignKey(Pays, on_delete=models.PROTECT)

    def __str__(self):
        return self.nom

    def json(self):
        return {
            "nom": self.nom,
            "taxe_immobiliere": self.taxe_immobiliere,
            "prix_m2": self.prix_m2,
            "pays": self.pays,
        }


class Machine(models.Model):
    nom = models.CharField(max_length=50)
    prix = models.FloatField()
    duree_de_vie = models.FloatField()  # en années
    cout_maintenance = models.FloatField()  # par an
    superficie = models.FloatField()  # en m^2

    def cost(self):
        return self.prix / self.duree_de_vie + self.cout_maintenance

    def __str__(self):
        return self.nom

    def json(self):
        return {
            "nom": self.nom,
            "prix": self.prix,
            "duree_de_vie": self.duree_de_vie,
            "cout_maintenance": self.cout_maintenance,
            "superficie": self.superficie,
        }


class QuantiteMachine(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
    nombre = models.IntegerField()

    def cost(self):
        return self.machine.cost() * self.nombre

    def __str__(self):
        return f"{self.machine.nom} x {self.nombre}"

    def json(self):
        return {"machine": self.machine, "nombre": self.nombre}


class Lieu(models.Model):
    nom = models.CharField(max_length=50)
    ville = models.ForeignKey(Ville, on_delete=models.PROTECT)
    superficie = models.FloatField()  # en m^2
    quantite_machines = models.ManyToManyField(Machine)
    consommation_electrique = models.FloatField()  # en W

    def cost(self):
        machines = sum(m.cost() for m in self.quantite_machines.all())
        return (
            +self.superficie * self.ville.prix_m2
            + self.consommation_electrique * self.ville.pays.tarif_electrique
            + machines
        )

    def __str__(self):
        return self.nom

    def json(self):
        return {
            "nom": self.nom,
            "ville": self.ville,
            "superficie": self.superficie,
            "quantite_machines": [v.pk for v in self.quantite_machines],
            "consommation_electrique": self.consommation_electrique,
        }


class Transport(models.Model):
    nombre_palettes = models.IntegerField()
    cout = models.FloatField()
    delai = models.FloatField()
    depart = models.ForeignKey(Lieu, on_delete=models.PROTECT, related_name="depart")
    arrivee = models.ForeignKey(Lieu, on_delete=models.PROTECT)

    def cost(self):
        return self.cout

    def __str__(self):
        return self.depart.nom + " to " + self.arrivee.nom

    def json(self):
        return {
            "nombre_palettes": self.nombre_palettes,
            "cout": self.cout,
            "delai": self.delai,
            "depart": self.depart,
            "arrivee": self.arrivee,
        }


class Operation(models.Model):
    nom = models.CharField(max_length=50)
    operation_suivante = models.ForeignKey(
        "self", blank=True, null=True, on_delete=models.PROTECT
    )
    cout = models.FloatField()
    machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
    quantite_produits = models.ForeignKey("QuantiteProduit", on_delete=models.PROTECT)
    heures_de_travail = models.FloatField()
    consomation_electrique = models.FloatField()

    def cost(self):
        return (
            self.cout
            + self.machine.quantitemachine_set.first()
            .lieu_set.first()
            .pays.salaire_minimum
            * self.heures_de_travail()
            + self.machine.quantitemachine_set.first()
            .lieu_set.first()
            .pays.tarif_electrique
            * self.consomation_electrique
        )

    def __str__(self):
        return self.nom

    def json(self):
        return {
            "nom": self.nom,
            "operation_suivante": self.operation_suivante,
            "cout": self.cout,
            "machine": self.machine,
            "quantite_produits": self.quantite_produits,
            "heures_de_travail": self.heures_de_travail,
            "consomation_electrique": self.consomation_electrique,
        }


class Produit(models.Model):
    nom = models.CharField(max_length=50)
    prix_de_vente = models.FloatField(blank=True, null=True)
    duree_de_vie = models.FloatField()
    nombre_par_palette = models.IntegerField()
    operations = models.ForeignKey(
        Operation, blank=True, null=True, on_delete=models.PROTECT
    )

    def cost(self):
        op = self.operations()
        c = 0
        while op:
            c += op.cos
        return c

    def __str__(self):
        return self.nom

    def json(self):
        return {
            "nom": self.nom,
            "prix_de_vente": self.prix_de_vente,
            "duree_de_vie": self.duree_de_vie,
            "nombre_par_palette": self.nombre_par_palette,
            "operations": self.operations,
        }


class PrixProduit(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.PROTECT)
    prix_achat = models.FloatField()

    def __str__(self):
        return f"{self.produit}: {self.prix_achat}"

    def json(self):
        return {"produit": self.produit, "prix_achat": self.prix_achat}


class Fournisseur(models.Model):
    nom = models.CharField(max_length=50)
    prix_produit = models.ForeignKey(PrixProduit, on_delete=models.PROTECT)

    def __str__(self):
        return self.nom

    def json(self):
        return {"nom": self.nom, "prix_produit": self.prix_produit}


class QuantiteProduit(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.PROTECT)
    nombre = models.IntegerField()

    def cost(self):
        return self.produit.cost() * self.nombre

    def __str__(self):
        return f"{self.produit} x {self.nombre}"

    def json(self):
        return {"produit": self.produit, "nombre": self.nombre}


class Stock(models.Model):
    quantite_produit = models.ForeignKey(QuantiteProduit, on_delete=models.PROTECT)
    palettes_max = models.IntegerField()

    def cost(self):
        return self.quantite_produit.cost()

    def __str__(self):
        return f"{self.quantite_produit}, palettes max: {self.palettes_max}"

    def json(self):
        return {
            "quantite_produit": self.quantite_produit,
            "palettes_max": self.palettes_max,
        }


class PointDeVente(models.Model):
    nom = models.CharField(max_length=50)
    lieu = models.ForeignKey(Lieu, on_delete=models.PROTECT)
    heures_de_travail = models.FloatField()
    stock = models.ForeignKey(Stock, on_delete=models.PROTECT)

    def cost(self):
        return (
            self.lieu.cost()
            + self.stock.cost()
            + self.heures_de_travail * self.lieu.ville.pays.salaire_minimum
        )

    def __str__(self):
        return self.nom

    def json(self):
        return {
            "nom": self.nom,
            "lieu": self.lieu,
            "heures_de_travail": self.heures_de_travail,
            "stock": self.stock,
        }


class Facture(models.Model):
    quantite_produit = models.ManyToManyField(QuantiteProduit)
    reduction = models.FloatField()
    point_de_vente = models.ForeignKey(PointDeVente, on_delete=models.PROTECT)
    client = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.quantite_produit}, reduction: {self.reduction}, à {self.point_de_vente} pour {self.client}"

    def json(self):
        return {
            "quantite_produit": self.quantite_produit,
            "reduction": self.reduction,
            "point_de_vente": self.point_de_vente,
            "client": self.client,
        }
