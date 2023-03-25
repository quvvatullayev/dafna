from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from dafna_app.models import (
    ManiImg,
)
from dafna_app.serializer import(
    ManiImgSerializers,
)

# Create your views here.

class AddMainImg(APIView):
    def post(self, request:Request):
        """
        input:json->
        {
            "img": str
        }
        return:json->
        {
            "id": int,
            "img": str
        }
        """
        data = request.data
        main_img = ManiImgSerializers(data=data)
        if main_img.is_valid():
            main_img.save()
            return Response(main_img.data)
        return Response(main_img.errors)
    
class DeleteMainImg(APIView):
    def get(self, request:Request, id):
        """
        input:get request /dafna_app/delete_main_img/id/
        return:{"OK delete":"200"}
        """
        main_img = ManiImg.objects.get(id = id)
        main_img.delete()
        return Response({"OK delete":"200"})
    
class GetMainImg(APIView):
    def get(self, request:Request):
        """
        input:get request /dafna_app/get_main_img/
        return:json->
        {
            "id": int,
            "img": str
        }
        """
        main_img = ManiImg.objects.all()
        main_img_serializers = ManiImgSerializers(main_img, many=True)
        return Response(main_img_serializers.data)