from django.db import models

# Create your models here.

class Katalog(models.Model):
    name = models.TextField(max_length=225)
    discrpition = models.CharField(max_length=225)
    img_url = models.TextField(max_length=225)

    def __str__(self) -> str:
        return self.name
    
class Prodouct_type(models.Model):
    name = models.CharField(max_length=225)
    img_url = models.TextField(max_length=225)
    katalog = models.ForeignKey(Katalog, models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Prodouct(models.Model):
    name = models.TextField(max_length=225)
    discrpition = models.CharField(max_length=225)
    img_url = models.TextField(max_length=225)
    price = models.IntegerField()
    color = models.TextField(max_length=25)
    manufacturer = models.TextField(max_length=25)
    material = models.TextField(max_length=25)
    prodouct_type = models.ForeignKey(Prodouct_type, models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
class Love(models.Model):
    prodouct = models.ForeignKey(Prodouct, models.CASCADE)

    def __str__(self) -> str:
        return self.prodouct.name
    
class Cart(models.Model):
    prodouct = models.ForeignKey(Prodouct, models.CASCADE)

    def __str__(self) -> str:
        return self.prodouct.name
    
class Video(models.Model):
    name = models.TextField(max_length=225)
    discrpition = models.CharField(max_length=225)
    video_url = models.TextField(max_length=225)

    def __str__(self) -> str:
        return self.name
    
class Main_contacts(models.Model):
    operator = models.TextField(max_length=25)
    menejer = models.TextField(max_length=25)
    mebel_menejer = models.TextField(max_length=25)
    guarantee = models.IntegerField(default=0)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.operator
    
class Contact(models.Model):
    branches_name = models.TextField(max_length=225)
    address = models.TextField(max_length=225)
    datetime = models.DateTimeField(auto_now=True, blank=True, null=True)
    menefer = models.TextField(max_length=225)
    main_contacts = models.ForeignKey(Main_contacts, models.CASCADE)

    def __str__(self) -> str:
        return self.branches_name
