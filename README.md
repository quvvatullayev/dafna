# Dafna doc


### Dafna
| method | endpoint | descriptoin |
|--------|----------|-------------|
| POST | `add_katalog/` | add katalog |
| POST | `updeate_katalog/` | updeate katalog |
| GET  | `get_katalog/` | get katalog |
| GET  | `delete_katalog/<int:id>/` | delete katalog | 
| POST | `add_prodouct_type/` | add prodouct tupe |
| POST | `updeate_prouduct_type/<int:id>/` | updeate prouduct type |
| GET  | `get_prodouct_type/<int:id>/` | get prodouct type |
| GET  | `delet_prodouct_tupe/<int:id>/` | delete prodouct type |
| POST | `add_prodouct/` | add prodouct |
| POST | `updeate_prodouct/<int:id>/` | updeate prodouct |
| GET  | `get_prodouct/<int:id>/` | get prodouct |
| GET  | `delete_prodouct/<int:id>/` | delete prodouct |
| POST | `add_love/` | add love |
| GET  | `delete_love/<int:id>/` | delete love |
| POST | `add_cart/` |add cart |
| GET  | `delete_cart/<int:id>/` | delete cart |
| GET  | `get_cart/` | get cart |
| GET  | `get_love/` | get love |
| POST | `add_video/` | add video |
| GET  | `delete_video/<int:id>/` | delete video |
| GET  | `get_video/` | get video |
| POST | `add_main_contact/` | add main contact |
| POST | `updeate_main_contact/<int:id>/` | updeate main contact |
| GET  | `get_main_contact/` | get main contact |
| GET  | `delet_main_contact/<int:id>/` | delet main contact |
| POST | `add_contact/` | add contact |
| POST | `updeate_contact/<int:id>/` | updeate contact |
| GET  | `delete_contact/<int:id>/` | delete contact |
| GET  | `get_contact/<int:id>/` | get contact |
| GET  | `sout/<int:id>/` | sorting products |
| GET  | `delete_all_cart/<int:id>/` | delete all cart |
<br><br>
<hr>



# Model
## you can find this image from [this link](https://app.diagrams.net/#G1Kt5Z4bO88bhWJrlhcsGTbzqfw991eCt7)
<img src='./dafna_model.png'>
<br><br><br><br>
<hr>

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
<hr>

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

**GET** ```dafna_app/delete_katalog/<int:id>/```
### url to delete the directory


```python
    input:get request dafna_app/delete_katalog/<id>/
    return:json->{"OK delete":"200"}
        
```
<hr>

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

**GET** ```dafna_app/delet_prodouct_tupe/<int:id>/```
### url to delete product type

```python
    input:get request dafna_app/delet_prodouct_tupe/id/
    return:json->{"OK delete":"200"}
        
```
<hr>

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

**GET** ```dafna_app/get_prodouct/<int:id>/```
### url to read prodouct


```python
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
```
<hr>

**GET** ```dafna_app/delete_prodouct/<int:id>/```
### url to delete prodouct


```python
    input:get request dafna_app/delete_prodouct/id/
    return:json->{"OK delete":"200"}
```
<hr>

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

**GET** ```dafna_app/delete_love/<int:id>/```
### url to delete love


```python
    input:get request /dafna_app/delete_love/id/
    return:{"OK delete":"200"}
        
```
<hr>

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

**GET** ```dafna_app/delete_cart/<int:id>/```
### url to delete cart


```python
    input:get request /dafna_app/delete_cart/id/
    return:{"OK delete":"200"}
```
<hr>

**GET** ```dafna_app/delete_all_cart/<int:id>/```
### url to delete all carts


```python
    input:get request /dafna_app/delete_all_cart/id/
    return:{"OK delete":"200"}
        
```
<hr>

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

**GET** ```dafna_app/get_love/```
### url to get loves


```python
        
```
<hr>

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

**GET** ```dafna_app/delete_video/<int:id>/```
### url to delete video

```python

        input:get request /dafna_app/delete_video/id/
        return:{"OK delete":"200"}
        
```
<hr>

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

**GET** ```dafna_app/delet_main_contact/<int:id>/```
### url to delete main contact


```python
        
        input:get request /dafna_app/delete_main_contact/id/
        return:{"OK delete":"200"}
```
<hr>

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

**GET** ```dafna_app/delete_contact/<int:id>/```
### url to delete contact

```python

        input:get request /dafna_app/delete_contact/id/
        return:{"OK delete":"200"}
        
```
<hr>

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

...
