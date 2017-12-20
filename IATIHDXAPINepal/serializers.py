from rest_framework import serializers
from .models import HXLData, IATIData, ShelterData


class HXLTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = HXLData        
        fields = '__all__'

class IATITestSerializer(serializers.ModelSerializer):
    class Meta:
        model = IATIData  
        fields = '__all__'

class ShelterItemsTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShelterData  
        fields = '__all__'

