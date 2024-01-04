from django.urls import path
from .views import *

urlpatterns = [
    path('customusers_list/', CustomUserListView.as_view()),
    path('customuser_registration/', CustomUserRegistrationCreateView.as_view()),
    path('customuser_login/', CustomUserLoginView.as_view()),                
]