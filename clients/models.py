from django.db import models


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    document = models.IntegerField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.first_name
