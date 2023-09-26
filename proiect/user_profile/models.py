from django.db import models


class Logs(models.Model):

    create_at = models.DateTimeField(auto_now_add=True, blank=True)    #se adauga automat, daca nu se adauga lasa gol
    update_at = models.DateTimeField(auto_now=True, blank=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    action = models.CharField(max_length=10)
    url = models.CharField(max_length=100)


class Pontaj(models.Model):

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)     #permitem sa nu existe end_date (poate nu s-a oprit pontajul)
