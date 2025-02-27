from rest_framework import serializers
from .models import User,Doctor,Patient,Appointment,Prescription,MedicineInventory,PrescribedMedicine
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']
        extra_kwargs = {'password': {'write_only': True}}


class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']

    def validate(self, attr):
        if attr['password1'] != attr['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attr

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data['role']
        )
        user.set_password(validated_data['password1'])
        user.save()
        return user



class DoctorSerializer(serializers.ModelSerializer):
    
    user = UserRegistrationSerializer()
    class Meta:
        model = Doctor
        fields = '__all__'
    
    def create(self, validated_data):
        
        user_data = validated_data.pop('user')
        
        # Create the User object using UserRegistrationSerializer
        user_serializer = UserRegistrationSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        # Create the Doctor object and link it to the User
        doctor = Doctor.objects.create(user=user, **validated_data)
        return doctor    

class PatientSerializer(serializers.ModelSerializer):
    user = UserRegistrationSerializer()
    class Meta:
        model = Patient
        fields = '__all__'
    
    def create(self, validated_data):
        # Extract the nested 'user' data
        user_data = validated_data.pop('user')
        
        # Create the User object using UserRegistrationSerializer
        user_serializer = UserRegistrationSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        # Create the Patient object and link it to the User
        patient = Patient.objects.create(user=user, **validated_data)
        return patient    
        
    def validate_contact_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Contact number should contain only digits.")
        return value    

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
