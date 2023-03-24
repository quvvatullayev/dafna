from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from base64 import b64decode
from django.contrib.auth import authenticate
from dafna_app.models import (
    Prodouct,
    Cart,
)
from dafna_app.serializer import(
    ProdouctSerializers,
    CartSerializers,
)

# Create your views here.

class AddCart(APIView):
    def post(self, request:Request):
        """
        input:json->
            {
                "prodouct": int
            }
        return:json->
            {
                "add cart":"ok"
            }
        """
        auth = request.headers.get('Authorization')
        token = auth.split(' ')[1]
        auth = b64decode(token).decode('utf-8')
        auth = auth.split(':')
        username, password = auth
        user = authenticate(username=username, password=password)

        if user is not None:
            data = request.data
            cart = CartSerializers(data=data)
            prodouct_filter = Prodouct.objects.get(id = data['prodouct'])
            prodouct = prodouct_filter
            prodouct.carts = True
            prodouct.save()
            if cart.is_valid():
                cart.save()
                return Response({ "add cart":"ok"})
            return Response(cart.errors)
        return Response({"error":"user not found"})

class DeleteCart(APIView):
    def get(self, request:Request, id):
        """
        input:get request /dafna_app/delete_cart/id/
        return:{"OK delete":"200"}
        """
        auth = request.headers.get('Authorization')
        token = auth.split(' ')[1]
        auth = b64decode(token).decode('utf-8')
        auth = auth.split(':')
        username, password = auth
        user = authenticate(username=username, password=password)

        if user is not None:
            cart = Cart.objects.get(id = id)
            prodouct_filter = Prodouct.objects.get(id = cart.prodouct.id)
            prodouct = prodouct_filter
            prodouct.carts = False
            prodouct.save()
            cart.delete()
            return Response({"OK delete":"200"})
        return Response({"error":"user not found"})
    
class DeleteAllCart(APIView):
    def get(self, request:Request, id):
        """
        input:get request /dafna_app/delete_all_cart/id/
        return:{"OK delete":"200"}
        """
        auth = request.headers.get('Authorization')
        token = auth.split(' ')[1]
        auth = b64decode(token).decode('utf-8')
        auth = auth.split(':')
        username, password = auth
        user = authenticate(username=username, password=password)

        if user is not None:
            cart_prodouct = Cart.objects.filter(prodouct = id)

            prodouct_filter = Prodouct.objects.get(id = id)
            prodouct = prodouct_filter
            prodouct.carts = False
            prodouct.save()
            
            if cart_prodouct:
                cart_prodouct.delete()
                return Response({"OK delete":"200"}) 
            return Response({})
        return Response({"error":"user not found"})

class GetCart(APIView):
    def get(self, request:Request):
        """
        input:get request
        return:json->
        {
            "carts": [
                {
                    "id": int,
                    "name": str,
                    "discrpition": str,
                    "img_url": str,
                    "price": int,
                    "color": str,
                    "like":bool,
                    "carts":bool,
                    "manufacturer": str,
                    "material": str,
                    "prodouct_type": int
                }
            ]
        }
        """
        auth = request.headers.get('Authorization')
        token = auth.split(' ')[1]
        auth = b64decode(token).decode('utf-8')
        auth = auth.split(':')
        username, password = auth
        user = authenticate(username=username, password=password)

        if user is not None:
            prodouct_filter = Prodouct.objects.filter(carts = True)
            prodouct = ProdouctSerializers(prodouct_filter, many = True)
            data = {
                "price_sum":0,
                'carts':[]
            }
            for i in prodouct.data:
                append_data = {
                    "id":i['id'],
                    "name":i['name'],
                    "discrpition":i['discrpition'],
                    "img_url":i['img_url'],
                    "price":i['price'],
                    "color":i['color'],
                    "like":i['like'],
                    "carts":i['carts'],
                    "manufacturer":i['manufacturer'],
                    "material":i['material'],
                    "prodouct_type":i['prodouct_type']
                }
                data['carts'].append(append_data)
                data['price_sum'] += i['price']

            return Response(data)
        return Response({"error":"user not found"})
