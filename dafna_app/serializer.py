from rest_framework import serializers
from .models import (
    Katalog,
    Prodouct, 
    Prodouct_type,
    Love,
    Cart,
    Video,
    Main_contacts,
    Contact,
    Prodouct_img,
)

class KatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Katalog
        fields = '__all__'

class ProdouctSerializers(serializers.ModelSerializer):
    class Meta:
        model = Prodouct
        fields = '__all__'

class ProdouctImgSerializers(serializers.ModelSerializer):
    class Meta:
        model = Prodouct_img
        fields = '__all__'

class ProdouctTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Prodouct_type
        fields = '__all__'

class LoveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Love
        fields = '__all__'

class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class VideoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class MainContactsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Main_contacts
        fields = '__all__'

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
