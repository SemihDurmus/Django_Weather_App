from django.urls import path
from .views import index, delete

urlpatterns = [
    path("", index, name="home"),
    path("<str:city>/delete/", delete, name="delete"),
]
