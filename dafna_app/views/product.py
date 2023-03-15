from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from dafna_app.models import (
    Katalog,
    Prodouct, 
    Prodouct_type,
    Prodouct_img,
)
from dafna_app.serializer import(
    KatalogSerializer,
    ProdouctSerializers,
    ProdouctTypeSerializers,
    ProdouctImgSerializers,
)

# Create your views here.

class AddProdouct(APIView):
    def post(self, request:Request):
        """
        input:json->
        {
            "name": str,
            "discrpition": str,
            "img_url":str
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
            "img_url":str,
            "price":int,
            "like":bool,
            "carts":bool,
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
            "img_url": (option)str,
            "price": (option)int,
            "color": (option)str,
            "like": (option)bool,
            "carts": (option)bool,
            "manufacturer": (option)str,
            "material": (option)str,
            "prodouct_type": (option)int
        }
        return:json->
        {
            "id": int,
            "name": str,
            "discrpition": str,
            "img_url":str,
            "price": int,
            "color":str,
            "like": bool,
            "carts": bool,
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
        updeate_prodouct.img_url = data.get('img_url', updeate_prodouct.img_url)
        updeate_prodouct.price = data.get('price', updeate_prodouct.price)
        updeate_prodouct.color = data.get('color', updeate_prodouct.color)
        updeate_prodouct.like = data.get('like', updeate_prodouct.like)
        updeate_prodouct.cart = data.get('cart', updeate_prodouct.cart)
        updeate_prodouct.manufacturer = data.get('manufacturer', updeate_prodouct.manufacturer)
        updeate_prodouct.material = data.get('material', updeate_prodouct.material)
        updeate_prodouct.save()
        prodouct = ProdouctSerializers(updeate_prodouct, many = False)
        return Response(prodouct.data)

class GetProdouct(APIView):
    def get(self, request:Request, id):
        """
        input:get request dafna_app/get_prodouct/id/
        return:json->
        {   
            "id":int,
            "name": str,
            "discrpition": str,
            "img_url": str,
            "prodouct_type": {
                "id":int,
                "name": str,
                "img_url": str,
                "prodoucts": [
                    {
                        "id": int,
                        "name": str,
                        "discrpition": str,
                        "img_url": str,
                        "price": int,
                        "color": str,
                        "like": bool,
                        "carts": bool,
                        "manufacturer": str,
                        "material": str,
                        "prodouct_type": int
                    }
                ]
            }
        }
        """
        prodouct_filter = Prodouct.objects.filter(prodouct_type = id)
        prodouct = ProdouctSerializers(prodouct_filter, many = True)
        prodouct_type_filter = Prodouct_type.objects.get(id = id)
        prodouct_type = ProdouctTypeSerializers(prodouct_type_filter, many = False)
        katalog_filter = Katalog.objects.get(id = prodouct_type.data['katalog'])
        katalog = KatalogSerializer(katalog_filter, many = False)
        data = {
            'id':katalog.data['id'],
            'name':katalog.data['name'],
            'discrpition':katalog.data['discrpition'],
            'img_url':katalog.data['img_url'],
            'prodouct_type':{
                "id":prodouct_type.data['id'],
                'name':prodouct_type.data['name'],
                'img_url':prodouct_type.data['img_url'],
                'prodoucts':prodouct.data
            }
        }

        return Response(data)

class DeleteProdouct(APIView):
    def get(self, request:Request, id):
        """
        input:get request dafna_app/delete_prodouct/id/
        return:json->{"OK delete":"200"}
        """
        prodouct = Prodouct.objects.get(id = id)
        prodouct.delete()
        return Response({"OK delete":"200"})

class Sort(APIView):
    def get(self, request:Request, name):
        """
        input:get request
        return:json->
        [
            "sorts":
            [
                {
                    "id": int,
                    "name": str,
                    "discrpition": str,
                    "img_url": str,
                    "price": int,
                    "color": str,
                    "manufacturer": int,
                    "like":boole,
                    "carts": boole,
                    "material": str,
                    "prodouct_type": int
                }
            ]
        ]

        or:json->
        {
            "sort": "None"
        }
        """
        prodouct_filter = Prodouct.objects.filter(name__contains = name)
        prodouct = ProdouctSerializers(prodouct_filter, many = True)
        if len(prodouct.data) > 0:
            data = {
                "sorts":prodouct.data
            }
            return Response(data)
        return Response({'sort':"None"})

class GetNewProduct(APIView):
    def get(self, request:Request):
        """
        input:get request
        return:json->
        {
            "prodoucts": [
                {
                    "id": int,
                    "name": str,
                    "discrpition": str
                    "img_url": str,
                    "price": int,
                    "color": str,
                    "manufacturer": str,
                    "like":bool
                    "material": str,
                    "prodouct_type": int
                }
            ]
        }
        """
        data = Prodouct.objects.all()[::-1][:10]
        prodouct = ProdouctSerializers(data, many = True)
        data = {'prodoucts':prodouct.data}
        return Response(data)

class GetRecommendationProdouct(APIView):
    def get(self, request:Request):
        """
        input:get request
        return:json->
        {
            "prodoucts": [
                {
                    "id": int,
                    "name": str,
                    "discrpition": str
                    "img_url": str,
                    "price": int,
                    "color": str,
                    "manufacturer": str,
                    "like":bool
                    "material": str,
                    "prodouct_type": int
                }
            ]
        }
        """
        data = Prodouct.objects.all()[:10]
        prodouct = ProdouctSerializers(data, many = True)
        data = {'prodoucts':prodouct.data}
        return Response(data)
    
class GetProdouctDetail(APIView):
    def get(self, request:Request, id):
        """
        input:get request
        return:json->
        {
            "prodouct": {
                "id": int,
                "name": str,
                "discrpition": str
                "img_url": str,
                "imgs": list,
                "price": int,
                "color": str,
                "manufacturer": str,
                "material": str,
                "like":bool
                "prodouct_type": int
            }
        }
        """
        prodouct_filter = Prodouct.objects.get(id = id)
        prodouct = ProdouctSerializers(prodouct_filter, many = False)
        prodouct_img_filter = Prodouct_img.objects.filter(prodouct = id)
        prodouct_img = ProdouctImgSerializers(prodouct_img_filter, many = True)
        data = {
            "prodouct":{
                "id":prodouct.data['id'],
                "name":prodouct.data['name'],
                "discrpition":prodouct.data['discrpition'],
                "img_url":prodouct.data['img_url'],
                "imgs":prodouct_img.data,
                "price":prodouct.data['price'],
                "color":prodouct.data['color'],
                "manufacturer":prodouct.data['manufacturer'],
                "material":prodouct.data['material'],  
                "like":prodouct.data['like'],
                "prodouct_type":prodouct.data['prodouct_type'],
            }
        }
        return Response(data)
