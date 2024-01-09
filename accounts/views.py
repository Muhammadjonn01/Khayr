from .serializers import *
from .models import *
from rest_framework.generics import *
from rest_framework.permissions import * 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate


class CustomUserRegistrationCreateView(CreateAPIView):
    permission_classes = [AllowAny] 
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserRegistrationCreateSerializer
    exclude = ("last_login", "is_superuser", "is_staff", "date_joined", "user_permissions", "is_active")

class CustomUserListView(ListAPIView):
    queryset = CustomUser.objects.all().order_by("-id")
    serializer_class = CustomUserListSerializer

class CustomUserLoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = CustomUserLoginSerializer
    def post(self, request):
        serializer = CustomUserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
 
        if authenticate(email=email, password=password): 
            if authenticate(email=email, password=password).is_active:  
                return Response({'detail': 'Login successful!'}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'The user account has been disabled.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Invalid username or password.'}, status=status.HTTP_400_BAD_REQUEST)