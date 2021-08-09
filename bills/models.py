from django.db import models


class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    client_id = models.ForeignKey('clients.Client', on_delete=models.SET_NULL, null=True)
    company_name = models.CharField(max_length=200)
    nit = models.IntegerField()
    code = models.IntegerField()

    def __str__(self):
        return self.company_name
