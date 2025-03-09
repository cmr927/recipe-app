from django.urls import path
from .views import home, records

app_name = 'home'

urlpatterns = [
    path('', home),
    path('home/', records)
]