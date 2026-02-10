from rest_framwork import serializers
from .model import productdata

class productserializer(serializers.ModelSerializer):
    class meta:
        model = productdata
        fields = '__all__'
        
