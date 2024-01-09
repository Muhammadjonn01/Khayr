from django.urls import path
from .views import *

urlpatterns = [
    path('donations_list/',DonationListView.as_view()),
    path('donation_create/',DonationCreateView.as_view()),
    path('getdonations_list/',GetDonationListView.as_view()),
    path('getdonation_create/',GetDonationCreateView.as_view()),
    path('comments_list/',CommentListView.as_view()),
    path('comment_create/',CommentCreateView.as_view()),
    path('imgs_list/',ImgListView.as_view()),
    path('img_create/',ImgCreateView.as_view()),
    path('search/',SearchGetDonationView.as_view()),
]
