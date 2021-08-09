from rest_framework.serializers import ModelSerializer

from bills.serializers import BillSerializer
from billsProducts.models import BillProduct
from products.serializers import ProductSerializer


class BillProductSerializer(ModelSerializer):
    bill_id = BillSerializer()
    product_id = ProductSerializer()

    class Meta:
        model = BillProduct
        fields = '__all__'


class CreateBillProductSerializer(ModelSerializer):
    class Meta:
        model = BillProduct
        fields = '__all__'
