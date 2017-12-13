from django.db import models

# Create your models here.
class jardin(models.Model):
    nom = models.CharField(max_length=60)
    adresse = models.CharField(max_length=100)
    ville = models.CharField(max_length=20)


    def __str__(self):
        return self.nom

class plante(models.Model):
    nom = models.CharField(max_length=45)
    date_naissance = models.DateField()
    date_deces = models.DateField()
    id_variete = models.ForeignKey('variete')
    id_jardin = models.ForeignKey('jardin')

    class Meta:
        ordering=['id_jardin']


    def __str__(self):
        return self.nom

class variete(models.Model):
    nom = models.CharField(max_length=25)

    def __str__(self):
        return self.nom
