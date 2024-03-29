from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Katalog(models.Model):
    name = models.TextField(max_length=225)
    discrpition = models.CharField(max_length=225)
    img_url = models.ImageField()

    def __str__(self) -> str:
        return self.name
    
class ManiImg(models.Model):
    img_url = models.ImageField()
    
class Prodouct_type(models.Model):
    name = models.CharField(max_length=225)
    img_url = models.ImageField()
    katalog = models.ForeignKey(Katalog, models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Prodouct(models.Model):
    name = models.TextField(max_length=225)
    discrpition = models.CharField(max_length=225)
    img_url = models.ImageField()
    price = models.IntegerField()
    like = models.BooleanField(default=False)
    carts = models.BooleanField(default=False)
    color = models.TextField(max_length=25)
    manufacturer = models.TextField(max_length=25)
    material = models.TextField(max_length=25)
    prodouct_type = models.ForeignKey(Prodouct_type, models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
class Prodouct_img(models.Model):
    img = models.ImageField()
    prodouct = models.ForeignKey(Prodouct, models.CASCADE)

    def __str__(self) -> str:
        return self.prodouct.name + 'imges'

class Imgs(models.Model):
    imgs = models.ImageField()
    
class Love(models.Model):
    prodouct = models.ForeignKey(Prodouct, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)

    def __str__(self) -> str:
        return self.prodouct.name
    
class Cart(models.Model):
    prodouct = models.ForeignKey(Prodouct, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)

    def __str__(self) -> str:
        return self.prodouct.name
    
class Video(models.Model):
    name = models.TextField(max_length=225)
    discrpition = models.CharField(max_length=225)
    video_url = models.TextField(max_length=225)

    def __str__(self) -> str:
        return self.name
    
class Main_contacts(models.Model):
    operator = models.CharField(max_length=252)
    menejer = models.CharField(max_length=252)
    mebel_menejer = models.CharField(max_length=252)
    guarantee = models.IntegerField(default=0)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.operator
    
class Contact(models.Model):
    branches_name = models.CharField(max_length=252)
    address = models.CharField(max_length=252)
    datetime = models.DateTimeField(auto_now=True, blank=True)
    menefer = models.CharField(max_length=252)
    main_contacts = models.ForeignKey(Main_contacts, models.CASCADE)

    def __str__(self) -> str:
        return self.branches_name
