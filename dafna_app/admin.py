from django.contrib import admin
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
    Imgs,  
)

# Register your models here.
admin.site.register([
    Katalog, 
    Prodouct, 
    Prodouct_type,
    Love,
    Cart,
    Video,
    Main_contacts,
    Contact,
    Prodouct_img,
    Imgs,
    ])
