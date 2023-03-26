from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
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

class DeleteCart(APIView):
    def get(self, request:Request, id):
        """
        input:get request /dafna_app/delete_cart/id/
        return:{"OK delete":"200"}
        """
        cart_filter = Cart.objects.filter(id = id)
        cart_filter = cart_filter.first()
        
        if cart_filter:
            cart = CartSerializers(cart_filter)
            prodouct_filter = Prodouct.objects.get(id = cart.data['prodouct'])
            prodouct = prodouct_filter
            prodouct.carts = False
            prodouct.save()
            cart_filter.delete()
            return Response({"OK delete":"200"})
        return Response({})
    
class DeleteAllCart(APIView):
    def get(self, request:Request, id):
        """
        input:get request /dafna_app/delete_all_cart/id/
        return:{"OK delete":"200"}
        """
        cart_prodouct = Cart.objects.filter(prodouct = id)

        prodouct_filter = Prodouct.objects.get(id = id)
        prodouct = prodouct_filter
        prodouct.carts = False
        prodouct.save()
        
        if cart_prodouct:
            cart_prodouct.delete()
            return Response({"OK delete":"200"}) 
        return Response({})

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
        cart_filter = Cart.objects.all()
        cart = CartSerializers(cart_filter, many = True)
        prodouct_filter = Prodouct.objects.filter(carts = True)
        prodouct = ProdouctSerializers(prodouct_filter, many = True)
        data = {
            "price_sum":0,
            'carts':[]
        }
        
        for i in cart.data:
            for j in prodouct.data:
                if i['prodouct'] == j['id']:
                    cart_appedn = {
                        "id": i['id'],
                        'prodouct': i['prodouct'],
                        "name": j['name'],
                        "discrpition": j['discrpition'],
                        "img_url": j['img_url'],
                        "price": j['price'],
                        "color": j['color'],
                        "like":j['like'],
                        "carts":j['carts'],
                        "manufacturer": j['manufacturer'],
                        "material": j['material'],
                        "prodouct_type": j['prodouct_type']
                        
                    }
                    data['carts'].append(cart_appedn)
                    data['price_sum'] += j['price']

        return Response(data)
