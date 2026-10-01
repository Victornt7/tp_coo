from django.core.management import call_command
from django.test import TestCase

from .models import (
    Lieu,
    Machine,
)


class MachineModelTests(TestCase):
    def test_machine_creation(self):
        self.assertEqual(Machine.objects.count(), 0)
        Machine.objects.create(
            nom="Encartoneuse",
            prix=12000,
            duree_de_vie=12 * 365,
            cout_maintenance=300,
            superficie=20,
        )
        self.assertEqual(Machine.objects.count(), 1)


class CoutLieuTest(TestCase):
    def test_cout_lieu(self):
        call_command("loaddata", "datatest.json")
        self.assertEqual(
            Lieu.objects.first().cost(), 7500480.0
        )  # Cout de la Velustrie, calculé égal à 7500480.0
