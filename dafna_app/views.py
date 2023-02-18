from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from .models import (
    Katalog,
    Prodouct, 
    Prodouct_type,
    Love,
    Cart,
    Video,
    Main_contacts,
    Contact
)
from .serializer import(
    KatalogSerializer,
    ProdouctSerializers,
    ProdouctTypeSerializers,
    LoveSerializers,
    CartSerializers,
    VideoSerializers,
    MainContactsSerializers,
    ContactSerializers,
)

# Create your views here.

class AddKatalog(APIView):
    def post(self, request:Request):
        """
        imput:
            {
                "name": str,
                "discrpition": str,
                "img_url":str
            }
        return: json ->
            {
                "id": int,
                "name":str,
                "discrpition": str,
                "img_url":str
            }
        """
        data = request.data
        katalog = KatalogSerializer(data=data)
        if katalog.is_valid():
            katalog.save()
            return Response(katalog.data)
        return Response(katalog.errors)
    
class UpdeateKatalog(APIView):
    def post(self, request:Request, id):
        """
        imput:
            {
                "name":(option) str ,
                "discrpition":(option) str,
                "img_url":(option)str
            }
        return: json ->
            {
                "id": int,
                "name":str
                "discrpition": str,
                "img_url":str
            }
        """
        filter_katalog = Katalog.objects.get(id = id)
        data = request.data
        updeate_katalog = filter_katalog
        updeate_katalog.name = data.get('name', updeate_katalog.name)
        updeate_katalog.discrpition = data.get('discrpition', updeate_katalog.discrpition)
        updeate_katalog.img_url = data.get('img_url', updeate_katalog.img_url)
        updeate_katalog.save()
        katalog = KatalogSerializer(updeate_katalog)
        return Response(katalog.data)

class GetKatalog(APIView):
    def get(self, request:Request):
        """
        input:get request
        return: json->
        {
            "katalogs": [
                {
                "id": int,
                "name":str
                "discrpition": str,
                "img_url":str
                }
            ]
        }
        """
        filter_katalog = Katalog.objects.all()
        katalog = KatalogSerializer(filter_katalog, many = True)
        data = {"katalogs":katalog.data}
        return Response(data)
    
class DeleteKatalog(APIView):
    def get(self, request:Request, id):
        """
        input:get request http://127.0.0.1:8000/dafna_app/delete_katalog/<id>/
        return:json->{"OK delete":"200"}
        """
        katalog = Katalog.objects.get(id = id)
        katalog.delete()
        return Response({"OK delete":"200"})

class AddProdouctType(APIView):
    def post(self, request:Request):
        """
        input:json->{
            "name": str,
            "img_url":str,
            "katalog":int katalog id int
            }
        return:json->{
            "id":int
            "name": str,
            "img_url":str,
            "katalog":int katalog id int
            }
        """
        data = request.data
        prodouct = ProdouctTypeSerializers(data=data)
        if prodouct.is_valid():
            prodouct.save()
            return Response(prodouct.data)
        return Response(prodouct.errors)

class UpdeateProdouctType(APIView):
    def post(self, request:Request, id):
        """
        input:json->
        {
            "name":(options)str,
            "img_url": (options)str,
        }
        return:json->
        {
            "id": int,
            "name":str,
            "img_url": str,
            "katalog": int
        }
        """
        filter_prodouct_type = Prodouct_type.objects.get(id = id)
        data = request.data
        prodouct_type = filter_prodouct_type
        prodouct_type.name = data.get('name', prodouct_type.name)
        prodouct_type.img_url = data.get('img_url', prodouct_type.img_url)
        prodouct_type.save()
        serializers_prodouct_type = ProdouctTypeSerializers(prodouct_type)
        return Response(serializers_prodouct_type.data)

class GetProdouctType(APIView):
    def get(self, request:Request, id):
        """intput:request get dafna_app/get_prodouct_type/id/
            return:json->
            {
                "id": int,
                "name":str,
                "discrpition": str,
                "img_url":str,
                "prodouct_typt": [
                    {
                        "id": int,
                        "name": str,
                        "img_url": str,
                        "katalog": int
                    },
                ]
            }
        """
        filter_prodouct_type = Prodouct_type.objects.filter(katalog = id)
        katalog_filter = Katalog.objects.get(id = id)
        katalog = KatalogSerializer(katalog_filter)
        prodouct_type = ProdouctTypeSerializers(filter_prodouct_type, many = True)
        data = {
            "id":katalog.data['id'],
            "name":katalog.data['name'],
            "discrpition":katalog.data['discrpition'],
            "img_url":katalog.data['img_url'],
            "prodouct_typt":prodouct_type.data

        }
        return Response(data)

class DeleteProdouctType(APIView):
    def get(self, request:Request, id):
        """
        input:get request dafna_app/delet_prodouct_tupe/id/
        return:json->{"OK delete":"200"}
        """
        prodouct_type = Prodouct_type.objects.get(id = id)
        prodouct_type.delete()
        return Response({"OK delete":"200"})

class AddProdouct(APIView):
    def post(self, request:Request):
        """
        input:json->
        {
            "name": str,
            "discrpition": str,
            "img_url":str
            "price":int,
            "color": str,
            "manufacturer":str,
            "material": str,
            "prodouct_type": int
        }
        return:json->
        {
            "id":int
            "name": str,
            "discrpition": str,
            "img_url":str,
            "price":int,
            "color": str,
            "manufacturer":str,
            "material": str,
            "prodouct_type": int
        }
        """
        data = request.data
        prodouct = ProdouctSerializers(data=data)
        if prodouct.is_valid():
            prodouct.save()
            return Response(prodouct.data)
        return Response(prodouct.errors)

class UpdeateProdouct(APIView):
    def post(self, request:Request, id):
        """
        input:post request
        {
            "name": (option)str,
            "discrpition": (option)str,
            "img_url": (option)str,
            "price": (option)int,
            "color": (option)str,
            "manufacturer": (option)str,
            "material": (option)str,
            "prodouct_type": (option)int
        }
        return:json->
        {
            "id": int,
            "name": str,
            "discrpition": str,
            "img_url":str,
            "price": int,
            "color":str,
            "manufacturer": str,
            "material": str,
            "prodouct_type": int
        }
        """
        filter_prodouct = Prodouct.objects.get(id = id)
        updeate_prodouct = filter_prodouct
        data = request.data
        updeate_prodouct.name = data.get('name', updeate_prodouct.name)
        updeate_prodouct.discrpition = data.get('discrpition', updeate_prodouct.discrpition)
        updeate_prodouct.img_url = data.get('img_url', updeate_prodouct.img_url)
        updeate_prodouct.price = data.get('price', updeate_prodouct.price)
        updeate_prodouct.color = data.get('color', updeate_prodouct.color)
        updeate_prodouct.manufacturer = data.get('manufacturer', updeate_prodouct.manufacturer)
        updeate_prodouct.material = data.get('material', updeate_prodouct.material)
        updeate_prodouct.save()
        prodouct = ProdouctSerializers(updeate_prodouct, many = False)
        return Response(prodouct.data)

class GetProdouct(APIView):
    def get(self, request:Request, id):
        """
        input:get request dafna_app/get_prodouct/id/
        return:json->
        {
            "name": str,
            "discrpition": str,
            "img_url": str,
            "prodouct_type": {
                "name": str,
                "img_url": str,
                "prodoucts": [
                    {
                        "id": int,
                        "name": str,
                        "discrpition": str,
                        "img_url": str,
                        "price": int,
                        "color": str,
                        "manufacturer": str,
                        "material": str,
                        "prodouct_type": int
                    }
                ]
            }
        }
        """
        prodouct_filter = Prodouct.objects.filter(prodouct_type = id)
        prodouct = ProdouctSerializers(prodouct_filter, many = True)
        prodouct_type_filter = Prodouct_type.objects.get(id = id)
        prodouct_type = ProdouctTypeSerializers(prodouct_type_filter, many = False)
        print(prodouct_type.data['katalog'])
        katalog_filter = Katalog.objects.get(id = prodouct_type.data['katalog'])
        katalog = KatalogSerializer(katalog_filter, many = False)
        data = {
            'name':katalog.data['name'],
            'discrpition':katalog.data['discrpition'],
            'img_url':katalog.data['img_url'],
            'prodouct_type':{
                'name':prodouct_type.data['name'],
                'img_url':prodouct_type.data['img_url'],
                'prodoucts':prodouct.data
            }
        }

        return Response(data)

class DeleteProdouct(APIView):
    def get(self, request:Request, id):
        """
        input:get request dafna_app/delete_prodouct/id/
        return:json->{"OK delete":"200"}
        """
        prodouct = Prodouct.objects.get(id = id)
        prodouct.delete()
        return Response({"OK delete":"200"})

class AddLove(APIView):
    def post(self, request:Request):
        """input:json->
            {
                "prodouct": int product id
            }
           return:json->
            {
                "prodouct": int product id
            } 
        """
        data = request.data
        love = LoveSerializers(data=data)
        if love.is_valid():
            love.save()
            return Response(love.data)
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
        love_filter = Love.objects.all()
        love = LoveSerializers(love_filter, many = True)
        data = {
            'loves':[]
        }
        for i in love.data:
            prodouct_filter = Prodouct.objects.get(id = i["prodouct"])
            prodouct = ProdouctSerializers(prodouct_filter)
            appendt_data = prodouct.data
            appendt_data['love_id'] = i['id']
            data['loves'].append(appendt_data)
        return Response(data)

class DeleteLove(APIView):
    def get(self, requeat:Request, id):
        """
        input:get request /dafna_app/delete_love/id/
        return:{"OK delete":"200"}
        """
        love = Love.objects.get(id=id)
        love.delete
        return Response({"OK delete":"200"})

class AddCart(APIView):
    def post(self, request:Request):
        """
        input:json->
            {
                "prodouct": int
            }
        return:json->
            {
                "id":int
                "prodouct": int
            }
        """
        data = request.data
        cart = CartSerializers(data=data)
        if cart.is_valid():
            cart.save()
            return Response(cart.data)
        return Response(cart.errors)

class DeleteCart(APIView):
    def get(self, request:Request, id):
        """
        input:get request /dafna_app/delete_cart/id/
        return:{"OK delete":"200"}
        """
        cart = Cart.objects.get(id = id)
        cart.delete()
        return Response({"OK delete":"200"})

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
                    "manufacturer": str,
                    "material": str,
                    "prodouct_type": int
                }
            ]
        }
        """
        cart_filter = Cart.objects.all()
        cart = CartSerializers(cart_filter, many = True)
        data = {
            'carts':[]
        }
        for i in cart.data:
            prodouct_filter = Prodouct.objects.get(id = i['prodouct'])
            prodouct = ProdouctSerializers(prodouct_filter, many = False)
            append_data = prodouct.data
            append_data['cart_id'] = i['id']
            data['carts'].append(append_data)
        return Response(data)

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
        video.delete
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
        main_contacts.delete
        return Response({"OK delete":"200"})

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
        updeate_contact.menefer = data.get("branches_name", updeate_contact.menefer)
        updeate_contact.main_contacts = data.get("branches_name", updeate_contact.main_contacts)
        updeate_contact.save()
        contact = ContactSerializers(updeate_contact)
        return Response(contact.data)

class DeleteContact(APIView):
    def get(self, request:Request, id):
        """
        input:get request /dafna_app/delete_contact/id/
        return:{"OK delete":"200"}
        """
        contacts = Contact.objects.get(id = id)
        contacts.delete
        return Response({"OK delete":"200"})






