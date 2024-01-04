from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers
from django.contrib.auth import authenticate

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
    


class CustomUserLoginSerializer(ModelSerializer):
    email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        fields = ['email', 'password'] 
    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:

            user = authenticate(email=email, password=password)
            
            if user:
                if user.is_active:
                    data['user'] = user
                    return data
                else:
                    raise serializers.ValidationError('The user account has been disabled.')
            else:
                raise serializers.ValidationError('Invalid username or password!')
        else:
            raise serializers.ValidationError('You must provide a username and password!')