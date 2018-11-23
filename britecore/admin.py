from django.contrib import admin

from .models import Datatypes, Risk

# Register your models here.

admin.site.register(Datatypes)
admin.site.register(Risk)