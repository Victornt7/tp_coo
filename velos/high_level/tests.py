from django.test import TestCase

from .models import Machine


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
