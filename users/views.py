from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from users.serializers import UserSerializer, CreateUserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateUserSerializer
        return UserSerializer





