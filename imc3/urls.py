

from django.urls import path
from .views import *

urlpatterns = [
    path('imc-script', ImcView.as_view(), name='imc-script')
]
