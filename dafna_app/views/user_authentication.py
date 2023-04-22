from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class CreateUser(APIView):
    def post(self, request: Request) -> Response:
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = User.objects.create(username=username, password=password)
        if user.check_password(password):
            token = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Something went wrong'})
    
class LogoutUser(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request: Request) -> Response:
        user = request.user
        token = Token.objects.get(user=user)
        token.delete()
        return Response({'message': 'User logged out'})
    
class LoginUser(APIView):
    def post(self, request: Request) -> Response:
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.get(username=username)
        if user.check_password(password):
            token = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Wrong credentials'})
