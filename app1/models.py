from django.db import models

class Formula1Teams(models.Model):
    name = models.TextField(max_length=30)
    country = models.TextField(max_length=30)
    driver1 = models.TextField(max_length=30)
    driver2 = models.TextField(max_length=30)
    car = models.TextField(max_length=30)

    def __str__(self):
        return self.name