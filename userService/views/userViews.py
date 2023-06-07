from rest_framework import generics
from rest_framework.generics import get_object_or_404

from ..serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from ..models import User


class UserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_url_kwarg = 'id_user'

    def get_object(self):
        id_user = self.kwargs.get(self.lookup_url_kwarg)
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=id_user)
        return obj

    def get_queryset(self):
        return User.objects.all()


class ConfidentialUserView(generics.RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer()

    def get_object(self):
        return self.request.user
