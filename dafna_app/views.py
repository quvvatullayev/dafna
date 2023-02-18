from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import (
    Katalog,
    Prodouct, 
    Prodouct_type,
    Love,
    Cart,
    Video,
    Main_contacts,
    Contact
)
from .serializer import(
    KatalogSerializer,
    ProdouctSerializers,
    ProdouctTypeSerializers,
    LoveSerializers,
    CartSerializers,
    VideoSerializers,
    MainContactsSerializers,
    ContactSerializers,
)

# Create your views here.

class AddKatalog(APIView):
    def post(self, request:Request):
        data = request.data
        katalog = KatalogSerializer(data=data)
        if katalog.is_valid():
            katalog.save()
            return Response(katalog.data)
        return Response(katalog.errors)
