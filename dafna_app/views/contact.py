from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from dafna_app.models import (
    Contact,
)
from dafna_app.serializer import(
    ContactSerializers,
)

# Create your views here.
class AddContact(APIView):
    def post(self, request:Request):
        """
        input:json->
        {
            "branches_name": str,
            "datetime":(option)ditetime,
            "address":str,
            "menefer": str,
            "main_contacts": int
        }
        return:json->
        {
            "id":int,
            "branches_name": str,
            "datetime":ditetime,
            "address":str,
            "menefer": str,
            "main_contacts": int
        }
        """
        data = request.data
        contact = ContactSerializers(data=data)
        if contact.is_valid():
            contact.save()
            return Response(contact.data)
        return Response(contact.errors)

class UpdeateContact(APIView):
    def post(self, request:Request, id):
        """
        input:json->
        {
            "branches_name": (option)str,
            "datetime":(option)ditetime,
            "address":(option)str,
            "menefer": (option)str,
            "main_contacts": (option)int
        }
        return:json->
        {
            "id":int,
            "branches_name": str,
            "datetime":ditetime,
            "address":str,
            "menefer": str,
            "main_contacts": int
        }"""
        data = request.data
        contact_filter = Contact.objects.get(id = id)
        updeate_contact = contact_filter
        updeate_contact.branches_name = data.get("branches_name", updeate_contact.branches_name)
        updeate_contact.address = data.get("address", updeate_contact.address)
        updeate_contact.datetime = data.get("datetime", updeate_contact.datetime)
        updeate_contact.menefer = data.get("menefer", updeate_contact.menefer)
        updeate_contact.main_contacts = data.get("main_contacts", updeate_contact.main_contacts)
        updeate_contact.save()
        contact = ContactSerializers(updeate_contact, many = False)
        return Response(contact.data)

class DeleteContact(APIView):
    def get(self, request:Request, id):
        """
        input:get request /dafna_app/delete_contact/id/
        return:{"OK delete":"200"}
        """
        contacts = Contact.objects.get(id = id)
        contacts.delete()
        return Response({"OK delete":"200"})

class GetContact(APIView):
    def get(self, request:Request):
        """
        input:get request
        return:json->
        {
            "contacts": [
                {
                    "id": int,
                    "branches_name": str,
                    "address": str,
                    "datetime": datetime str,
                    "menefer": str,
                    "main_contacts": int
                }
            ]
        }
        """
        contact_all = Contact.objects.all()
        contact = ContactSerializers(contact_all, many = True)
        data = {
            'contacts':contact.data
        }
        return Response(data)
