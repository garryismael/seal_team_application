from django.urls import path

from api.views.client import ClientListCreate


urlpatterns = [path("", ClientListCreate.as_view())]
