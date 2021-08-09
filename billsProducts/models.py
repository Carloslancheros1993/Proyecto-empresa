from django.db import models

class BillProduct(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey('bills.Bill',on_delete=models.SET_NULL, null=True)
    product_id = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True)