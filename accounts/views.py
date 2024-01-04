from .serializers import *
from .models import *
from rest_framework.generics import *
from rest_framework.permissions import * 

class CustomUserRegistrationCreateView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserRegistrationCreateSerializer
    exclude = ("last_login", "is_superuser", "is_staff", "date_joined", "user_permissions", "is_active")


class CustomUserLoginCreateView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserLoginCreateSerializer


class CustomUserListView(ListAPIView):
    queryset = CustomUser.objects.all().order_by("-id")
    serializer_class = CustomUserListSerializer
