from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from billsProducts.models import BillProduct
from billsProducts.serializers import BillProductSerializer, CreateBillProductSerializer


class BillProductGenericView(generics.ListCreateAPIView):
    queryset = BillProduct.objects.all()
    serializer_class = BillProductSerializer


class BillProductDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BillProduct.objects.all()
    serializer_class = BillProductSerializer
