from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='patient')
    def __str__(self):
        return self.username
class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    
    def __str__(self):
        return self.user.username
    
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    medical_history = models.TextField() 
    def __str__(self):
        return self.user.username
     
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    class Meta:
        unique_together = ('doctor', 'appointment_time')


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    medicine = models.CharField(max_length=255)
    dosage = models.CharField(max_length=255)
    

class MedicineInventory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    stock = models.IntegerField()
    price_per_unit = models.FloatField()

class PrescribedMedicine(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    medicine = models.ForeignKey(MedicineInventory, on_delete=models.CASCADE)
    quantity = models.IntegerField()            