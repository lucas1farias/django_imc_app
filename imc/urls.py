

from django.urls import path
from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('imc', imc, name='imc'),
    path('imc-app-result', imc_result, name='imc-app-result'),
]
