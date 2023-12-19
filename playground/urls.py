from django.urls import path
from . import views

# URL configration
urlpatterns = [
    path('prediction/', views.llmprediction)
]