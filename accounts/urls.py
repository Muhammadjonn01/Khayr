from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)


urlpatterns = [
    path('users/', CustomUserListView.as_view()),
    path('registration/', CustomUserRegistrationCreateView.as_view()),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),



    # path('customuser_login/', CustomUserLoginView.as_view()),                
]