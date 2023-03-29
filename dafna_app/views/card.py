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
        # Each product is in one, but how many there are in total is written in the cart
        """
            input:get request /dafna_app/get_cart/
            return:json->
            {
                "cart_price_sum":int,
                "cart":[
                    {   
                        "price_sum":int,
                        "prodouct_count":int,
                        "prodouct":[
                            {
                                "id": int,
                                "prodouct":int
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
                ]
            }
        """
        cart = Cart.objects.all()
        cart = CartSerializers(cart, many=True)
        pk_prodouct = {}
        for i in cart.data:
            if pk_prodouct.get(i['prodouct']):
                pk_prodouct[i['prodouct']] += 1
            else:
                pk_prodouct[i['prodouct']] = 1
    
        data = {
            "cart_price_sum":0,
            "cart":[]
        }
        
        for pk in pk_prodouct:
            append_prodouct = {
                "price_sum":0,
                "prodouct_count":0,
                "prodouct":[]
            }
            prodouct = Prodouct.objects.get(id = pk)
            prodouct = ProdouctSerializers(prodouct)
            prodouct = prodouct.data
            append_prodouct['price_sum'] = prodouct['price'] * pk_prodouct[pk]
            append_prodouct['prodouct_count'] = pk_prodouct[pk]
            append_prodouct["prodouct"].append(prodouct)
            data['cart_price_sum'] += prodouct['price']*pk_prodouct[pk]
            data["cart"].append(append_prodouct)

        return Response(data=data)
        
