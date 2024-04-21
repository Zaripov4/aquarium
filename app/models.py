from django.db import models


class Aquarium(models.Model):
    height = models.IntegerField()
    width = models.IntegerField()


class Fish(models.Model):
    aquarium = models.ForeignKey(Aquarium, on_delete=models.CASCADE)
    x_position = models.IntegerField()
    y_position = models.IntegerField()
    gender = models.CharField(max_length=10)
    lifespan = models.IntegerField()
