from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from dafna_app.models import (
    Main_contacts,
)
from dafna_app.serializer import(
    MainContactsSerializers,
)

# Create your views here.
class AddMainContact(APIView):
    def post(self, request:Request):
        """
        input:json->
        {
            "operator": str,
            "menejer": str,
            "mebel_menejer": str,
            "guarantee":int,
            "email": str email
        }
        return:json->
        {
            "id":int,
            "operator": str,
            "menejer": str,
            "mebel_menejer": str,
            "guarantee":int,
            "email": str email
        }
        """
        data = request.data
        main_contacts = MainContactsSerializers(data=data)
        if main_contacts.is_valid():
            main_contacts.save()
            return Response(main_contacts.data)
        return Response(main_contacts.errors)

class UpdeateMainContact(APIView):
    def post(self, request:Request, id):
        """
        input:json->
        {
            "operator": str,
            "menejer": str,
            "mebel_menejer":str,
            "guarantee": int,
            "email": str email
        }
        return:json->
        {
            "id": int,
            "operator": str,
            "menejer": str,
            "mebel_menejer":str,
            "guarantee": int,
            "email": str email
        }
        """
        data = request.data
        main_contacts_filter = Main_contacts.objects.get(id = id)
        updeate_m_c = main_contacts_filter
        updeate_m_c.operator = data.get('operator', updeate_m_c.operator)
        updeate_m_c.menejer = data.get("menejer", updeate_m_c.menejer)
        updeate_m_c.mebel_menejer = data.get("mebel_menejer", updeate_m_c.mebel_menejer)
        updeate_m_c.guarantee = data.get("guarantee", updeate_m_c.guarantee)
        updeate_m_c.email = data.get("email", updeate_m_c.email)
        updeate_m_c.save()
        main_contacts = MainContactsSerializers(updeate_m_c, many = False)
        return Response(main_contacts.data)

class GetMainContact(APIView):
    def get(self, request:Request):
        """
        input:get request
        return:json->
        {
            "main_contacts": [
                {
                    "id": int,
                    "operator": str,
                    "menejer": str,
                    "mebel_menejer": str,
                    "guarantee": int,
                    "email":str email
                }
            ]
        }
        """
        main_contacts_all = Main_contacts.objects.all()
        main_contacts = MainContactsSerializers(main_contacts_all, many = True)
        data = {
            "main_contacts":main_contacts.data
        }
        return Response(data)

class DeleteMainContact(APIView):
    def get(self, request:Request, id):
        """
        input:get request /dafna_app/delete_main_contact/id/
        return:{"OK delete":"200"}
        """
        main_contacts = Main_contacts.objects.get(id = id)
        main_contacts.delete()
        return Response({"OK delete":"200"})
