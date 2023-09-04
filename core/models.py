from django.db import models

class Offerte(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    adres = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)
    woonplaats = models.CharField(max_length=100)
    telefoon_nummer = models.CharField(max_length=15)
    services = models.ManyToManyField('Service', blank=True)
    uw_aanvraag = models.TextField()

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class StucProject(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.ImageField(upload_to='stucwerk/')\
    
    def __str__(self):
        return self.title

class PaintingProject(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.ImageField(upload_to='painting/')

    def __str__(self):
        return self.title

class SierpleisterProject(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.ImageField(upload_to='sierpleister/')

    def __str__(self):
        return self.title

class LijstwerkProject(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.ImageField(upload_to='lijstwerk/')

    def __str__(self):
        return self.title
    
class SausProject(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.ImageField(upload_to='sauzen/')

    def __str__(self):
        return self.title
    

