from django.db import models

class Formula1Teams(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    driver1 = models.CharField(max_length=30)
    driver2 = models.CharField(max_length=30)
    car = models.CharField(max_length=30)

    def __str__(self):
        return self.name