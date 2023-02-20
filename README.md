# Dafna doc


### Dafna
<h1>base url <a href='https://ogabek007.pythonanywhere.com'><u><i>https://ogabek007.pythonanywhere.com/</i></a></a></h1>

| method | endpoint | descriptoin |
|--------|----------|-------------|
| POST | <a href = "#0">`add_katalog/`</a>| add katalog |
| POST | <a href = "#1">`updeate_katalog/`</a> | updeate katalog |
| GET  | <a href = "#2">`get_katalog/`</a> | get katalog |
| GET  | <a href = "#3">`delete_katalog/<int:id>/`</a> | delete katalog | 
| POST | <a href = "#4">`add_prodouct_type/`</a> | add prodouct tupe |
| POST | <a href = "#5">`updeate_prouduct_type/<int:id>/` | updeate prouduct type |
| GET  | <a href = "#6">`get_prodouct_type/<int:id>/`</a> | get prodouct type |
| GET  | <a href = "#7">`delet_prodouct_tupe/<int:id>/`</a> | delete prodouct type |
| POST | <a href = "#8">`add_prodouct/`</a> | add prodouct |
| POST | <a href = "#9">`updeate_prodouct/<int:id>/`</a> | updeate prodouct |
| GET  | <a href = "#10">`get_prodouct/<int:id>/`</a> | get prodouct |
| GET  | <a href = "#11">`delete_prodouct/<int:id>/`</a> | delete prodouct |
| POST | <a href = "#12">`add_love/`</a> | add love |
| GET  | <a href = "#13">`delete_love/<int:id>/`</a> | delete love |
| POST | <a href = "#14">`add_cart/`</a> |add cart |
| GET  | <a href = "#15">`delete_cart/<int:id>/`</a> | delete cart |
| GET  | <a href = "#16">`get_cart/`</a> | get cart |
| GET  | <a href = "#17">`get_love/`</a> | get love |
| POST | <a href = "#18">`add_video/`</a> | add video |
| GET  | <a href = "#19">`delete_video/<int:id>/`</a> | delete video |
| GET  | <a href = "#20">`get_video/`</a> | get video |
| POST | <a href = "#21">`add_main_contact/`</a> | add main contact |
| POST | <a href = "#22">`updeate_main_contact/<int:id>/`</a> | updeate main contact |
| GET  | <a href = "#23">`get_main_contact/`</a> | get main contact |
| GET  | <a href = "#24">`delet_main_contact/<int:id>/`</a> | delet main contact |
| POST | <a href = "#25">`add_contact/`</a> | add contact |
| POST | <a href = "#26">`updeate_contact/<int:id>/`</a> | updeate contact |
| GET  | <a href = "#27">`delete_contact/<int:id>/`</a> | delete contact |
| GET  | <a href = "#28">`get_contact/<int:id>/`</a> | get contact |
| GET  | <a href = "#39">`sout/<int:id>/`</a> | sorting products |
| GET  | <a href = "#30">`delete_all_cart/<int:id>/`</a> | delete all cart |
| GET  | <a href = "#31">`sout/<str:name>/`</a> | url to search for products to buy |
<br><br>
<hr>



# Model
## you can find this image from [this link](https://app.diagrams.net/#G1Kt5Z4bO88bhWJrlhcsGTbzqfw991eCt7)
<img src='./dafna_model.png'>
<br><br><br><br>
<hr>

<div id="0"> 

**POST** ```dafna_app/add_katalog/```
### url to add directory


```python
        input:
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
        
```
</div>
<hr>

<div id="1">
 
**POST** ```dafna_app/updeate_katalog/<int:id>/```
### url to update directory


```python

        input:
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
        
```
<hr>
</div>
<div id="2">
 
**GET** ```dafna_app/get_katalog/```
### url to get all of the directory


```python
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
        
```
<hr>
</div>
<div id="3">
 
**GET** ```dafna_app/delete_katalog/<int:id>/```
### url to delete the directory


```python
    input:get request dafna_app/delete_katalog/<id>/
    return:json->{"OK delete":"200"}
        
```
<hr>
</div>
<div id="4">
 
**POST** ```dafna_app/add_prodouct_type/```
### url to add product type
 
```python

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
        
```
<hr>
</div>
<div id="5">
 
**POST** ```dafna_app/updeate_prouduct_type/<int:id>/```
### url to update product type

```python

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
        
```
<hr>
</div>
<div id="6">
 
**GET** ```dafna_app/get_prodouct_type/<int:id>/```
### url to get the product type

```python
        input:request get dafna_app/get_prodouct_type/id/
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
        
```
<hr>
</div>
<div id="7">
 
**GET** ```dafna_app/delet_prodouct_tupe/<int:id>/```
### url to delete product type

```python
    input:get request dafna_app/delet_prodouct_tupe/id/
    return:json->{"OK delete":"200"}
        
```
<hr>
</div>
<div id="8">
 
**POST** ```dafna_app/add_prodouct/```
### url to create the product


```python
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
```
<hr>
</div>
<div id="9">
 
**POST** ```dafna_app/updeate_prodouct/<int:id>/```
### url to update prodouct


```python
        
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
```
<hr>
</div>
<div id="10">
 
**GET** ```dafna_app/get_prodouct/<int:id>/```
### url to read prodouct


```python
    input:get request dafna_app/get_prodouct/id/
    return:json->
        
        input:get request dafna_app/get_prodouct/id/
        return:json->
        {   
            "id":int,
            "name": str,
            "discrpition": str,
            "img_url": str,
            "prodouct_type": {
                "id":int,
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
```
<hr>
</div>
<div id="11">
 
**GET** ```dafna_app/delete_prodouct/<int:id>/```
### url to delete prodouct


```python
    input:get request dafna_app/delete_prodouct/id/
    return:json->{"OK delete":"200"}
```
<hr>
</div>
<div id="12">
 
**POST** ```dafna_app/add_love/```
### url to add love


```python
    input:json->
            {
                "prodouct": int product id
            }
    return:json->
            {
                "id":int
                "prodouct": int product id
            }      
```
<hr>
</div>
<div id="13">
 
**GET** ```dafna_app/get_love/```
### url to get love


```python
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
        
```
<hr>
</div>
<div id="14">
 
**GET** ```dafna_app/delete_love/<int:id>/```
### url to delete love


```python
    input:get request /dafna_app/delete_love/id/
    return:{"OK delete":"200"}
        
```
<hr>
</div>
<div id="15">
 
**POST** ```dafna_app/add_cart/```
### url to add cart


```python
    input:json->
            {
                "prodouct": int
            }
    return:json->
            {
                "add cart":"ok"
            }
        
```
<hr>
</div>
<div id="16">
 
**GET** ```dafna_app/delete_cart/<int:id>/```
### url to delete cart


```python
    input:get request /dafna_app/delete_cart/id/
    return:{"OK delete":"200"}
```
<hr>
</div>
<div id="17">
 
**GET** ```dafna_app/delete_all_cart/<int:id>/```
### url to delete all carts


```python
    input:get request /dafna_app/delete_all_cart/id/
    return:{"OK delete":"200"}
        
```
<hr>
</div>
<div id="18">
 
**GET** ```dafna_app/get_cart/```
### url to get carts


```python
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
```
<hr>
</div>
<div id="19">
 
**GET** ```dafna_app/get_love/```
### url to get loves


```python
        
```
<hr>
</div>
<div id="20">
 
**POST** ```dafna_app/add_video/```
### url to add video


```python
        
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
```
<hr>
</div>
<div id="21">
 
**GET** ```dafna_app/delete_video/<int:id>/```
### url to delete video

```python

        input:get request /dafna_app/delete_video/id/
        return:{"OK delete":"200"}
        
```
<hr>
</div>
<div id="22">
 
**GET** ```dafna_app/get_video/```
### url to get video

```python
        
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
```
<hr>
</div>
<div id="23">
 
**POST** ```dafna_app/add_main_contact/```
### url to create main contact


```python

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
        
```
<hr>
</div>
<div id="24">
 
**POST** ```dafna_app/updeate_main_contact/<int:id>/```
### url to updeate main contact


```python

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
        
```
<hr>
</div>
<div id="25">
 
**GET** ```dafna_app/get_main_contact/```
### url to get main contact


```python
        
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
```
<hr>
</div>
<div id="26">
 
**GET** ```dafna_app/delet_main_contact/<int:id>/```
### url to delete main contact


```python
        
        input:get request /dafna_app/delete_main_contact/id/
        return:{"OK delete":"200"}
```
<hr>
</div>
<div id="27">
 
**POST** ```dafna_app/add_contact/```
### url to create contact


```python
        
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
```
<hr>
</div>
<div id="28">
 
**POST** ```dafna_app/updeate_contact/<int:id>/```
### url to updeate contact

```python
        
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
        }
```
<hr>
</div>
<div id="29">
 
**GET** ```dafna_app/delete_contact/<int:id>/```
### url to delete contact

```python

        input:get request /dafna_app/delete_contact/id/
        return:{"OK delete":"200"}
        
```
<hr>
</div>
<div id="30">
 
**GET** ```dafna_app/get_contact/```
### url to get contact

```python
        
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
```
<hr>
</div>
<div id="31">
 
**GET** ```dafna_app/sout/<str:name>/```
### url to search for products to buy


```python
        
        input:get request
        return:json->
        [
            {
                "id": int,
                "name": str,
                "discrpition": str,
                "img_url": str,
                "price": int,
                "color": str,
                "manufacturer": int,
                "material": str,
                "prodouct_type": int
            }
        ]

        or:json->
        {
            "sort": "None"
        }
```
<hr>
</div>

...
