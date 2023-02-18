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
]