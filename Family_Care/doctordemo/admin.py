from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Doctor_profiles)
admin.site.register(Education)
admin.site.register(Documents) 

# admin.site.register(Diagnostic)
