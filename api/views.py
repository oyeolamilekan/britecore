from django.shortcuts import render
from rest_framework import viewsets, pagination, generics
from .serializers import RiskSerailizer
from britecore.models import Risk


# Create your views here.

class RiskView(generics.ListAPIView):
    queryset = Risk.objects.all()
    serializer_class = RiskSerailizer
    
class RetriveRisk(generics.RetrieveAPIView):
    queryset = Risk.objects.all()
    serializer_class = RiskSerailizer