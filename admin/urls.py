from django.urls import path 
from .views import (
    index, 
)

app_name = 'admin'

urlpatterns = [
    path('', index, name='index'),
]