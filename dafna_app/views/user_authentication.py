from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication