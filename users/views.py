from django.contrib.auth.signals import user_logged_out
from django.contrib.auth.models import update_last_login

from rest_framework import generics, permissions, status, HTTP_HEADER_ENCODING
from rest_framework.response import Response

from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer

from .auth import TokenAuthentication

# Create your views here.


# process login and register request
def process_login_register(self, request, action):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    if action == 'register':
        user = serializer.save()
    elif action == 'login':
        user = serializer.validated_data

    response = Response({
        'user': UserSerializer(user, context=self.get_serializer_context()).data,
        'token': AuthToken.objects.create(user)[1],
    })

    token = response.data['token']
    del response.data['token']
    response.set_cookie(
        'auth_token',
        token,
        # domain='',
        # path='/',
        # samesite='Strict',
        # secure=True,
        httponly=False,
    )

    user = TokenAuthentication().authenticate_credentials(
        token.encode(HTTP_HEADER_ENCODING))[0]
    update_last_login(sender=user.__class__, user=user)

    return response


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        return process_login_register(self, request, action='register')


# Login API
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        return process_login_register(self, request, action='login')


# User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserSerializer

    def post(self, request, format=None):
        user = request.user
        response = Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
        })
        return response


# Custom Logout API
class LogoutAPI(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        request._auth.delete()
        user_logged_out.send(sender=request.user.__class__,
                             request=request, user=request.user)
        response = Response(None, status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie('auth_token', path='/', domain=None)
        return response