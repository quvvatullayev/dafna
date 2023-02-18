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
        input:get request
        return: json->
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

class AddProdouctType(APIView):
    def post(self, request:Request):
        """
        input:json->{
            "name": str,
            "img_url":str,
            "katalog":int katalog id int
            }
        return:json->{
            "id":int
            "name": str,
            "img_url":str,
            "katalog":int katalog id int
            }
        """
        data = request.data
        prodouct = ProdouctTypeSerializers(data=data)
        if prodouct.is_valid():
            prodouct.save()
            return Response(prodouct.data)
        return Response(prodouct.errors)

class UpdeateProdouctType(APIView):
    def post(self, request:Request, id):
        """
        input:json->
        {
            "name":(options)str,
            "img_url": (options)str,
        }
        return:json->
        {
            "id": int,
            "name":str,
            "img_url": str,
            "katalog": int
        }
        """
        filter_prodouct_type = Prodouct_type.objects.get(id = id)
        data = request.data
        prodouct_type = filter_prodouct_type
        prodouct_type.name = data.get('name', prodouct_type.name)
        prodouct_type.img_url = data.get('img_url', prodouct_type.img_url)
        prodouct_type.save()
        serializers_prodouct_type = ProdouctTypeSerializers(prodouct_type)
        return Response(serializers_prodouct_type.data)

class GetProdouctType(APIView):
    def get(self, request:Request, id):
        """intput:request get dafna_app/get_prodouct_type/id/
            return:json->
            {
                "id": int,
                "name":str,
                "discrpition": str,
                "img_url":str,
                "prodouct_typt": [
                    {
                        "id": int,
                        "name": str,
                        "img_url": str,
                        "katalog": int
                    },
                ]
            }
        """
        filter_prodouct_type = Prodouct_type.objects.filter(katalog = id)
        katalog_filter = Katalog.objects.get(id = id)
        katalog = KatalogSerializer(katalog_filter)
        prodouct_type = ProdouctTypeSerializers(filter_prodouct_type, many = True)
        data = {
            "id":katalog.data['id'],
            "name":katalog.data['name'],
            "discrpition":katalog.data['discrpition'],
            "img_url":katalog.data['img_url'],
            "prodouct_typt":prodouct_type.data

        }
        return Response(data)

class DeleteProdouctType(APIView):
    def get(self, request:Request, id):
        """
        input:get request dafna_app/delet_prodouct_tupe/id/
        return:json->{"OK delete":"200"}
        """
        prodouct_type = Prodouct_type.objects.get(id = id)
        prodouct_type.delete()
        return Response({"OK delete":"200"})

class AddProdouct(APIView):
    def post(self, request:Request):
        """
        input:json->
        {
            "name": str,
            "discrpition": str,
            "price":int,
            "color": str,
            "manufacturer":str,
            "material": str,
            "prodouct_type": int
        }
        return:json->
        {
            "id":int
            "name": str,
            "discrpition": str,
            "price":int,
            "color": str,
            "manufacturer":str,
            "material": str,
            "prodouct_type": int
        }
        """
        data = request.data
        prodouct = ProdouctSerializers(data=data)
        if prodouct.is_valid():
            prodouct.save()
            return Response(prodouct.data)
        return Response(prodouct.errors)

class UpdeateProdouct(APIView):
    def post(self, request:Request, id):
        """
        input:post request
        {
            "name": (option)str,
            "discrpition": (option)str,
            "price": (option)int,
            "color": (option)str,
            "manufacturer": (option)str,
            "material": (option)str,
            "prodouct_type": (option)int
        }
        return:json->
        {
            "id": int,
            "name": str,
            "discrpition": str,
            "price": int,
            "color":str,
            "manufacturer": str,
            "material": str,
            "prodouct_type": int
        }
        """
        filter_prodouct = Prodouct.objects.get(id = id)
        updeate_prodouct = filter_prodouct
        data = request.data
        updeate_prodouct.name = data.get('name', updeate_prodouct.name)
        updeate_prodouct.discrpition = data.get('discrpition', updeate_prodouct.discrpition)
        updeate_prodouct.price = data.get('price', updeate_prodouct.price)
        updeate_prodouct.color = data.get('color', updeate_prodouct.color)
        updeate_prodouct.manufacturer = data.get('manufacturer', updeate_prodouct.manufacturer)
        updeate_prodouct.material = data.get('material', updeate_prodouct.material)
        updeate_prodouct.save()
        prodouct = ProdouctSerializers(updeate_prodouct, many = False)
        return Response(prodouct.data)








