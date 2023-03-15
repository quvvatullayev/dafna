from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from dafna_app.models import (
    Prodouct,
    Love,
)
from dafna_app.serializer import(
    ProdouctSerializers,
    LoveSerializers,
)

# Create your views here.

class AddLove(APIView):
    def post(self, request:Request):
        """input:json->
            {
                "prodouct": int product id
            }
           return:json->
            {
                "id":int
                "prodouct": int product id
            } 
        """
        data = request.data
        love = LoveSerializers(data=data)
        love_all = Love.objects.all()
        love_all_data = LoveSerializers(love_all, many = True)
        id = data['prodouct']
        prodouct_filter = Prodouct.objects.get(id = id)
        prodouct = prodouct_filter
        if prodouct.like == True:
            prodouct.like = False
        else:
            prodouct.like = True
        prodouct.save()
        prodouct_list = []
        for i in love_all_data.data:
            prodouct_list.append(i['prodouct'])
        
        if love.is_valid() and data['prodouct'] not in prodouct_list:
            love.save()
            return Response(love.data)
        else:
            love_filter = Love.objects.get(prodouct = data['prodouct'])
            love_filter.delete()
        return Response(love.errors)

class GetLove(APIView):
    def get(self, request:Request):
        """
        input:get request
        return:json->
        {
            "loves": [
                {
                    "id": 5,
                    "name": "Aylanadigan stol",
                    "discrpition": "Ofis uchun Aylanadigan stollar to'plam",
                    "img_url": "nada",
                    "price": 4500000,
                    "color": "qora",
                    "manufacturer": "uz",
                    "material": "charim",
                    "prodouct_type": 3,
                    "love_id": 1
                }
            ]
        }
        """
        love_filter = Prodouct.objects.filter(like = True)
        love = ProdouctSerializers(love_filter, many = True)
        data = {
            'loves':love.data
        }
        return Response(data)

class DeleteLove(APIView):
    def get(self, requeat:Request, id):
        """
        input:get request /dafna_app/delete_love/id/
        return:{"OK delete":"200"}
        """
        love = Love.objects.get(id=id)
        love.delete()
        return Response({"OK delete":"200"})
