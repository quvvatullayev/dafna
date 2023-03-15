from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from dafna_app.models import (
    Prodouct_img,
)
from dafna_app.serializer import(
    ProdouctImgSerializers,
)

# Create your views here.

class AddProdouctImg(APIView):
    def post(self, request:Request, id):
        """
        input:post request
        {
            "img_url": str,
            "prodouct": int
        }
        return:json->
        {
            "id": int,
            "img_url": str,
            "prodouct": int
        }
        """
        data = request.data
        prodouct_img = ProdouctImgSerializers(data=data)
        if prodouct_img.is_valid():
            prodouct_img.save()
            return Response(prodouct_img.data)
        return Response(prodouct_img.errors)
    
class GetProdouctImg(APIView):
    def get(self, request:Request, id):
        """
        input:get request dafna_app/get_prodouct_img/id/
        return:json->
        {
            "imgs": [
                {
                    "id": int,
                    "img_url": str,
                    "prodouct": int
                }
            ]
        }
        """
        prodouct_img_filter = Prodouct_img.objects.filter(prodouct = id)
        prodouct_img = ProdouctImgSerializers(prodouct_img_filter, many = True)
        data = {
            "imgs": prodouct_img.data
        }
        return Response(data)
    
class DeleteProdouctImg(APIView):
    def get(self, request:Request, id):
        """
        input:get request dafna_app/delete_prodouct_img/id/
        return:json->{"OK delete":"200"}
        """
        prodouct_img = Prodouct_img.objects.get(id = id)
        prodouct_img.delete()
        return Response({"OK delete":"200"})
