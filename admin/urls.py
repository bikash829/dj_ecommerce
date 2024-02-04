from django.urls import path 
from .views import (
    index, 
    widgets,
    calendar,

    # general UI
    general,
)

app_name = 'admin'

urlpatterns = [
    path('', index, name='index'),
    path('widgets/',widgets, name='widgets'),
    path('calendar/',calendar, name='calendar'),

    # UI Elements
    path('general/',general, name='general'),
]