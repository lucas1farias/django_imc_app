

from django.contrib import admin
from .models import *


@admin.register(Imc)
class ImcAdmin(admin.ModelAdmin):
    list_display = (
        'result',
    )
