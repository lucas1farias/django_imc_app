

from django.urls import path
from .views import *

urlpatterns = [
    path('imc2', ImcView.as_view(), name='imc2')
]
