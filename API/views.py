from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import cayxanhserializers
from rest_framework import viewsets
from .models.cayxanhmodels import Cayxanh


class dscayxanh(viewsets.GenericViewSet, ListCreateAPIView):
    serializer_class = cayxanhserializers
    queryset = Cayxanh.objects.using('DoThi').all()