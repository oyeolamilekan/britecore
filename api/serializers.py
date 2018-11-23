from rest_framework import serializers
from britecore.models import Risk,Datatypes


class RiskSerailizer(serializers.ModelSerializer):
    datatypes = serializers.StringRelatedField(many=True)

    class Meta:
        model = Risk
        fields = ('id','title','datatypes')