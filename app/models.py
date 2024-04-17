from django.db import models

class Fish(models.Model):
    def __init__(self, gender, lifespan):
        self.gender = gender
        self.lifespan = lifespan
