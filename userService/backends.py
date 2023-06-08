from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model


class UserBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username=username)
            if user.password != password:
                return None
        except UserModel.DoesNotExist:
            return None
        return user
