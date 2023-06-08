from userService.models import User
from userService.serializer import AuthUserSerializer, UserSerializer, UpdateUserSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny


class UpdateUserView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        username = self.request.user
        obj = User.objects.get(username=username)
        return obj

    def get_serializer_context(self):
        context = {
            'request': self.request,
        }
        body = self.request.data
        fields = list(body.keys())
        if fields:
            context['fields'] = fields

        return context


class CheckTokenView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    serializer_class = AuthUserSerializer

    def post(self, request):
        user = request.user
        serialize_user = UserSerializer(user, context={'mode': 'conf_user'})
        token = request.auth
        return Response({'token': str(token), **serialize_user.data})


class SignUserView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            serializer_user = UserSerializer(user, context={'mode': 'conf_user'})
            return Response({"token": token.key, **serializer_user.data})

        return Response({'username': [''], 'password': [''], 'message': ['Неверный логин или пароль']},
                        status=status.HTTP_401_UNAUTHORIZED)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AuthUserSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            serializer_user = UserSerializer(user, context={'mode': 'conf_user'})
            token, _ = Token.objects.get_or_create(user=user)
            response = Response({'token': token.key, **serializer_user.data}, status=status.HTTP_201_CREATED)
            response.set_cookie('auth_token', token.key)
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
