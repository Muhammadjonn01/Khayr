from .serializers import *
from .models import *
from rest_framework.generics import *
from rest_framework.permissions import * 
from rest_framework.response import Response
from rest_framework import status

#This view show list of donations
class DonationListView(ListAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationListSerializer
    # permission_classes =[IsAuthor,IsAdminUser]
    
#This view create donation
class DonationCreateView(CreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationCreateSerializer
    # permission_classes = [IsAuthor]

#This view show list of getdonations
class GetDonationListView(ListAPIView):
    queryset = GetDonation.objects.all()
    serializer_class = GetDonationListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    
#This view create getdonation
class GetDonationCreateView(CreateAPIView):
    queryset = GetDonation.objects.all()
    serializer_class = GetDonationCreateSerializer
    # permission_classes = [IsAuthor]


class CommentListView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
#This view create donation
class CommentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]


class ImgListView(ListAPIView):
    queryset = Img.objects.all()
    serializer_class = ImgListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

class ImgCreateView(CreateAPIView):
    queryset = Img.objects.all()
    serializer_class = ImgCreateSerializer
    # permission_classes = [IsAuthenticated,IsAuthor]


class SearchGetDonationView(ListAPIView):
    queryset = GetDonation.objects.all().order_by('like')
    serializer_class = SearchGetDonationSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        query = self.request.GET.get('q', None)
        if query is not None:
            return GetDonation.objects.filter(description__icontains=query, )
        return None