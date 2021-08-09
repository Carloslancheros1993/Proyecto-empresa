from rest_framework.serializers import ModelSerializer

from bills.models import Bill
from clients.serializers import ClientSerializer


class BillSerializer(ModelSerializer):
    client_id = ClientSerializer()

    class Meta:
        model = Bill
        fields = '__all__'


class CreateBillSerializer(ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'
