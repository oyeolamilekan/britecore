from django.urls import path, include
from rest_framework import routers
from .views import RiskView,RetriveRisk


urlpatterns = [
    path('r_risk/', RiskView.as_view()),
    path('r_risk/<int:pk>/', RetriveRisk.as_view())
]
