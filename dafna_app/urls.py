from django.urls import path
from .views import(
    AddKatalog,
    UpdeateKatalog,
    GetKatalog,
    DeleteKatalog,
    AddProdouctType,
    UpdeateProdouctType,
    GetProdouctType,
    DeleteProdouctType,
    AddProdouct,
    UpdeateProdouct,
    GetProdouct,
    DeleteProdouct,
    AddLove,
    DeleteLove,
    AddCart,
    DeleteCart,
    GetCart,
    GetLove,
    AddVideo,
    DeleteVideo,
    GetVideo,
    UpdeateMainContact,
    UpdeateMainContact,
    GetMainContact,
    DeleteMainContact,
    AddContact,
    UpdeateContact,
    DeleteContact,
)

urlpatterns = [
    path('add_katalog/', AddKatalog.as_view()),
    path('updeate_katalog/<int:id>/', UpdeateKatalog.as_view()),
    path('get_katalog/', GetKatalog.as_view()),
    path('delete_katalog/<int:id>/', DeleteKatalog.as_view()),
    path('add_prodouct_type/', AddProdouctType.as_view()),
    path('updeate_prouduct_type/<int:id>/', UpdeateProdouctType.as_view()),
    path('get_prodouct_type/<int:id>/', GetProdouctType.as_view()),
    path('delet_prodouct_tupe/<int:id>/', DeleteProdouctType.as_view()),
    path('add_prodouct/', AddProdouct.as_view()),
    path('updeate_prodouct/<int:id>/', UpdeateProdouct.as_view()),
    path('get_prodouct/<int:id>/', GetProdouct.as_view()),
    path('delete_prodouct/<int:id>/', DeleteProdouct.as_view()),
    path('add_love/', AddLove.as_view()),
    path('delete_love/<int:id>/', DeleteLove.as_view()),
    path('add_cart/', AddCart.as_view()),
    path('delete_cart/<int:id>/', DeleteCart.as_view()),
    path('get_cart/', GetCart.as_view()),
    path('get_love/', GetLove.as_view()),
    path('add_video/', AddVideo.as_view()),
    path('delete_video/<int:id>/', DeleteVideo.as_view()),
    path('get_video/', GetVideo.as_view()),
    path('add_main_contact/', UpdeateMainContact.as_view()),
    path('updeate_main_contact/<int:id>/', UpdeateMainContact.as_view()),
    path('get_main_contact/', GetMainContact.as_view()),
    path('delet_main_contact/<int:id>/', DeleteMainContact.as_view()),
    path('add_contact/', AddContact.as_view()),
    path('updeate_contact/<int:id>/', UpdeateContact.as_view()),
    path('delete_contact/<int:id>/', DeleteContact.as_view())
]