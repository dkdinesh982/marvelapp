from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(NurseData)
admin.site.register(NurseReportdata)
admin.site.register(Doctor_at_home)

admin.site.register(Diagnostcms)
admin.site.register(Electrocardgram)
admin.site.register(Speciality)
admin.site.register(HospitalRegister)
admin.site.register(Fees)