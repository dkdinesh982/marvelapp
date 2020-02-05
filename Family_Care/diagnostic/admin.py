from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Diagnostic)

admin.site.register(Diagnostic_detail)