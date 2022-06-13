from django.db import models

# Create your models here.

class Region(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Coworking(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    url = models.TextField(max_length=100, null=True, blank=True)
    content = models.TextField(max_length=500, null=True, blank=True)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Accommodation(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    url = models.TextField(max_length=100, null=True, blank=True)
    content = models.TextField(max_length=500, null=True, blank=True)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    near_coworking_spaces = models.ManyToManyField(Coworking, related_name='Near_Accommodations', null=True, blank=True)

    def __str__(self):
        return self.name