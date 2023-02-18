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
        """
        imput:
            {
                "name": str,
                "discrpition": str,
                "img_url":str
            }
        return: json ->
            {
                "id": int,
                "name":str,
                "discrpition": str,
                "img_url":str
            }
        """
        data = request.data
        katalog = KatalogSerializer(data=data)
        if katalog.is_valid():
            katalog.save()
            return Response(katalog.data)
        return Response(katalog.errors)
    
class UpdeateKatalog(APIView):
    def post(self, request:Request, id):
        """
        imput:
            {
                "name":(option) str ,
                "discrpition":(option) str,
                "img_url":(option)str
            }
        return: json ->
            {
                "id": int,
                "name":str
                "discrpition": str,
                "img_url":str
            }
        """
        filter_katalog = Katalog.objects.get(id = id)
        data = request.data
        updeate_katalog = filter_katalog
        updeate_katalog.name = data.get('name', updeate_katalog.name)
        updeate_katalog.discrpition = data.get('discrpition', updeate_katalog.discrpition)
        updeate_katalog.img_url = data.get('img_url', updeate_katalog.img_url)
        updeate_katalog.save()
        katalog = KatalogSerializer(updeate_katalog)
        return Response(katalog.data)

class GetKatalog(APIView):
    def get(self, request:Request):
        """
        {
            "katalogs": [
                {
                "id": int,
                "name":str
                "discrpition": str,
                "img_url":str
                }
            ]
        }
        """
        filter_katalog = Katalog.objects.all()
        katalog = KatalogSerializer(filter_katalog, many = True)
        data = {"katalogs":katalog.data}
        return Response(data)
    
class DeleteKatalog(APIView):
    def get(self, request:Request, id):
        """
        input:get request http://127.0.0.1:8000/dafna_app/delete_katalog/<id>/
        return:json->{"OK delete":"200"}
        """
        katalog = Katalog.objects.get(id = id)
        katalog.delete()
        return Response({"OK delete":"200"})



