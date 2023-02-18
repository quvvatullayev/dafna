from django.urls import path
from .views import(
    AddKatalog,
)

urlpatterns = [
    path('add_katalog/', AddKatalog.as_view()),
]