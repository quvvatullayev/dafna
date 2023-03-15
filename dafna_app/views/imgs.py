from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from dafna_app.models import (
    Imgs,
)
from dafna_app.serializer import(
    ImgsSerializers,
)



class AddImg(APIView):
    def post(self, request:Request):
        """
        input:post request with json->
        {
            "imgs":str
        }
        return:json->
        {
            "id": int,
            "imgs": str,
        }
        """
        imgs = ImgsSerializers(data = request.data)
        if imgs.is_valid():
            imgs.save()
            return Response(imgs.data)
        return Response(imgs.errors)

class GetImg(APIView):
    def get(self, request:Request):
        """
        input:get request
        return:json->
        {
            "imgs": [
                {
                    "id": int,
                    "imgs": str,
                }
            ]
        }
        """
        imgs_filter = Imgs.objects.all()
        imgs = ImgsSerializers(imgs_filter, many = True)
        data = {
            "imgs":imgs.data
        }
        return Response(data)
    
class DeleteImg(APIView):
    def get(self, request:Request, id):
        """
        input:get request
        return:json->
        {
            "OK delete": "200"
        }
        """
        imgs_filter = Imgs.objects.get(id = id)
        imgs_filter.delete()
        return Response({"OK delete":"200"})