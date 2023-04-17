from django.urls import path
from .views.katalog import(
    AddKatalog,
    UpdeateKatalog,
    GetKatalog,
    DeleteKatalog,
)

urlpatterns = [
    path('add_katalog/', AddKatalog.as_view()),
    path('updeate_katalog/<int:id>/', UpdeateKatalog.as_view()),
    path('get_katalog/', GetKatalog.as_view()),
    path('delete_katalog/<int:id>/', DeleteKatalog.as_view()),
]

from .views.product_type import(
    AddProdouctType,
    UpdeateProdouctType,
    GetProdouctType,
    DeleteProdouctType,
)

urlpatterns += [
    path('add_prodouct_type/', AddProdouctType.as_view()),
    path('updeate_prouduct_type/<int:id>/', UpdeateProdouctType.as_view()),
    path('get_prodouct_type/<int:id>/', GetProdouctType.as_view()),
    path('delet_prodouct_tupe/<int:id>/', DeleteProdouctType.as_view()),
]

from .views.product import(
    AddProdouct,
    UpdeateProdouct,
    GetProdouct,
    DeleteProdouct,
    GetNewProduct,
    GetRecommendationProdouct,
    GetProdouctDetail,
    Sort,
)

urlpatterns += [
    path('add_prodouct/', AddProdouct.as_view()),
    path('updeate_prodouct/<int:id>/', UpdeateProdouct.as_view()),
    path('get_prodouct/<int:id>/', GetProdouct.as_view()),
    path('delete_prodouct/<int:id>/', DeleteProdouct.as_view()),
    path('sort/<str:name>/', Sort.as_view()),
    path('get_new_prodouct/', GetNewProduct.as_view()),
    path("get_rescommentations/", GetRecommendationProdouct.as_view()),
    path("get_prodouct_detail/<int:id>/", GetProdouctDetail.as_view()),
]

from .views.product_img import(
    AddProdouctImg,
    DeleteProdouctImg,
    GetProdouctImg,
)

urlpatterns += [
    path("add_prodouct_img/", AddProdouctImg.as_view()),
    path("delete_prodouct_img/<int:id>/", DeleteProdouctImg.as_view()),
    path("get_prodouct_img/<int:id>/", GetProdouctImg.as_view()),
]

from .views.imgs import(
    AddImg,
    DeleteImg,
    GetImg,
)

urlpatterns += [
    path("add_img/", AddImg.as_view()),
    path("delete_img/<int:id>/", DeleteImg.as_view()),
    path("get_img/", GetImg.as_view()),
]

from .views.video import(
    AddVideo,
    DeleteVideo,
    GetVideo,
)

urlpatterns += [
    path('add_video/', AddVideo.as_view()),
    path('delete_video/<int:id>/', DeleteVideo.as_view()),
    path('get_video/', GetVideo.as_view()),
]

from .views.main_contact import(
    AddMainContact,
    UpdeateMainContact,
    GetMainContact,
    DeleteMainContact,
)

urlpatterns += [
    path('add_main_contact/', AddMainContact.as_view()),
    path('updeate_main_contact/<int:id>/', UpdeateMainContact.as_view()),
    path('get_main_contact/', GetMainContact.as_view()),
    path('delet_main_contact/<int:id>/', DeleteMainContact.as_view()),
]

from .views.contact import(
    AddContact,
    UpdeateContact,
    GetContact,
    DeleteContact,
)

urlpatterns += [
    path('add_contact/', AddContact.as_view()),
    path('updeate_contact/<int:id>/', UpdeateContact.as_view()),
    path('delete_contact/<int:id>/', DeleteContact.as_view()),
    path('get_contact/', GetContact.as_view()),
]

from .views.love_view import(
    AddLove,
    DeleteLove,
    GetLove,
)

urlpatterns += [
    path('add_love/', AddLove.as_view()),
    path('delete_love/<int:id>/', DeleteLove.as_view()),
    path('get_love/', GetLove.as_view()),
]

from .views.card import(
    AddCart,
    DeleteCart,
    GetCart,
    DeleteAllCart,
)

urlpatterns += [
    path('add_cart/', AddCart.as_view()),
    path('delete_cart/<int:id>/', DeleteCart.as_view()),
    path('get_cart/', GetCart.as_view()),
    path('delete_all_cart/<int:id>/', DeleteAllCart.as_view()),
]

from .views.main_img import (
    AddMainImg,
    DeleteMainImg,
    GetMainImg,
)

urlpatterns += [
    path('add_main_img/', AddMainImg.as_view()),
    path('delete_main_img/<int:id>/', DeleteMainImg.as_view()),
    path('get_main_img/', GetMainImg.as_view()),
]

from .views.user_authentication import(
    CreateUser,
    LoginUser,
    LogoutUser,
)

urlpatterns += [
    path('create_user/', CreateUser.as_view()),
    path('login_user/', LoginUser.as_view()),
    path('logout_user/', LogoutUser.as_view()),
]