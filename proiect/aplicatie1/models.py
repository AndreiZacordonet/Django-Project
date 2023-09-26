from django.db import models

# !! aceasta clasa modeleaza baza de date !!


class Locations(models.Model):      # numele de clasa are Litera mare

    city = models.CharField(max_length=100)
    country = models.CharField(max_length=150)
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.city} - {self.country}"

