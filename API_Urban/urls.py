from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url,include
from rest_framework import routers


# router = routers.SimpleRouter()
# router.register(r'getListTencx', getTenCX, base_name="List Ten Cay Xanh")

urlpatterns = [
    url(r'^api/', include("API.urls"))
]
