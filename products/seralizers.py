from rest_framwork import serializers
from .models import productdata

class productserializer(serializers.ModelSerializer):
    class Meta:
        model = productdata
        fields = '__all__'
        
