from django.urls import path
from .views import *

urlpatterns = [
    path('userchoises_list/',UserChoiceListView.as_view()),
    path('userchoise_create/',UserChoiceCreateView.as_view()),
    path('donations_list/',DonationListView.as_view()),
    path('donation_create/',DonationCreateView.as_view()),
    path('getdonations_list/',GetDonationListView.as_view()),
    path('getdonation_create/',GetDonationCreateView.as_view()),
    path('comments_list/',CommentListView.as_view()),
    path('comment_create/',CommentCreateView.as_view()),
    path('files_list/',FileListView.as_view()),
    path('file_create/',FileCreateView.as_view()),
]
