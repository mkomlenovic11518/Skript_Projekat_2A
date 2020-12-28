from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Proizvodjac(models.Model):
    naziv_proizvodjac=models.CharField(max_length=64)
    sifra_proizvodjac = models.CharField(max_length=5)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.naziv_proizvodjac


class Roba(models.Model):
    naziv_robe=models.CharField(max_length=64)
    sifra_robe=models.CharField(max_length=5)
    kolicina=models.IntegerField(default=0)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    proizvodjac=models.ForeignKey(Proizvodjac,on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

