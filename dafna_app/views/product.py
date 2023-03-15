from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from dafna_app.models import (
    Katalog,
    Prodouct_type,
)
from dafna_app.serializer import(
    KatalogSerializer,
    ProdouctTypeSerializers,
)

# Create your views here.

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
