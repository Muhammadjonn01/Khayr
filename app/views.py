from .serializers import *
from .models import *
from rest_framework.generics import *
from rest_framework.permissions import * 

#This views are for Movies CRUD
class UserChoiceListView(ListAPIView):
    queryset = UserChoice.objects.all()
    serializer_class = UserChoiceListSerializer   
    

class UserChoiceCreateView(CreateAPIView):
    queryset = UserChoice.objects.all()
    serializer_class = UserChoiceCreateSerializer


class DonationListView(ListAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationListSerializer
    

class DonationCreateView(CreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationCreateSerializer


class GetDonationListView(ListAPIView):
    queryset = GetDonation.objects.all()
    serializer_class = GetDonationListSerializer
    

class GetDonationCreateView(CreateAPIView):
    queryset = GetDonation.objects.all()
    serializer_class = GetDonationCreateSerializer


class CommentListView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    

class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer


class FileListView(ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileListSerializer
    

class FileCreateView(CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileCreateSerializer