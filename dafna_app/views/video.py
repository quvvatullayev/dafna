from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from dafna_app.models import (
    Video,
)
from dafna_app.serializer import(
    VideoSerializers,
)

# Create your views here.

class AddVideo(APIView):
    def post(self, request:Request):
        """
        input:json->
        {
            "name": str,
            "discrpition": str,
            "video_url": str
        }
        return:json->
        {
            "id": 1,
            "name": str,
            "discrpition": str,
            "video_url": str
        }
        """
        data = request.data
        video = VideoSerializers(data=data)
        if video.is_valid():
            video.save()
            return Response(video.data)
        return Response(video.errors)

class DeleteVideo(APIView):
    def get(self, request:Request, id):
        """
        input:get request /dafna_app/delete_video/id/
        return:{"OK delete":"200"}
        """
        video = Video.objects.get(id = id)
        video.delete()
        return Response({"OK delete":"200"})

class GetVideo(APIView):
    def get(self, request:Request):
        """
        input:get request
        return:json->
        {
            "videos": [
                {
                    "id": int,
                    "name": str,
                    "discrpition":str,
                    "video_url": str
                }
            ]
        }
        """
        video_filter = Video.objects.all()
        video = VideoSerializers(video_filter, many = True)
        data = {
            'videos':video.data
        }
        return Response(data)
