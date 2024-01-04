from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers

class CustomUserListSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        queryset = CustomUser.objects.all()
        fields = "__all__"

class CustomUserRegistrationCreateSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        exclude = ("last_login", "is_superuser", "is_staff", "user_permissions", "is_active","groups")
    
    def validate(self, data):
        if data["password"] != data["password2"]:
            raise Exception("Passwords do not match.")
        
        return data

    def create(self, validated_data):
        del validated_data["password2"]
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
    

class CustomUserLoginCreateSerializer(ModelSerializer):
    pass