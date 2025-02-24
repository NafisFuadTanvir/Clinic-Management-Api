from rest_framework import serializers
from .models import User,Doctor,Patient,Appointment,Prescription,MedicineInventory,PrescribedMedicine

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'

class MedicineInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineInventory
        fields = '__all__'

class PrescribedMedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescribedMedicine
        fields = '__all__'
