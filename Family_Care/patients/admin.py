from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Patients)
admin.site.register(Family_Patients)
admin.site.register(Report)