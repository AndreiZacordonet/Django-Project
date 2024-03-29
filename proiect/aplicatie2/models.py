from django.db import models

tipuri_companie = (('SRL', 'S.R.L.'), ('SA', 'S.A.'))


class Companies(models.Model):

    nume = models.CharField(max_length=100)
    website = models.CharField(max_length=50)
    tip_companie = models.CharField(max_length=10, choices=tipuri_companie)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nume} - {self.tip_companie}"
