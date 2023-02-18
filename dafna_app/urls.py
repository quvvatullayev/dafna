from django.urls import path
from .views import(
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