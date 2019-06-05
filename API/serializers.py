from API.models.cayxanhmodels import Cayxanh
from rest_framework import serializers

class cayxanhserializers(serializers.ModelSerializer):
    class Meta:
        model = Cayxanh
        fields = ('sohieu', )