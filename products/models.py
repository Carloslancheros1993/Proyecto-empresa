from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    attribute4 = models.BooleanField()

    def __str__(self):
        return self.name
