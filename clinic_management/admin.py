from django.contrib import admin
from .models import User,Doctor,Patient,Appointment,Prescription,PrescribedMedicine,MedicineInventory
# Register your models here.
admin.site.register(User)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(MedicineInventory)
admin.site.register(PrescribedMedicine)

