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
    url = models.TextField(max_length=100)
    content = models.TextField(max_length=500, null=True)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Accommodation(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    url = models.TextField(max_length=100)
    content = models.TextField(max_length=500, null=True)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    near_coworking_spaces = models.ManyToManyField(Coworking, related_name='Near_Accommodations')

    def __str__(self):
        return self.name