from rest_framework.serializers import ModelSerializer
from .models  import *
from accounts.serializers import *


class DonationListSerializer(ModelSerializer):
    class Meta:
        model = Donation
        fields = "__all__"

class GetDonationListSerializer(ModelSerializer):
    class Meta:
        model = GetDonation
        fields = "__all__"

class CommentListSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class ImgListSerializer(ModelSerializer):
    class Meta:
        model = Img
        fields = "__all__"


class DonationCreateSerializer(ModelSerializer):
    class Meta:
        model = Donation
        fields = "__all__"

    def save(self, **kwargs):
        donation = super().save(**kwargs)
        getdonation = donation.getdonation
        getdonation.current_amount += donation.donation_amount
        getdonation.save()


class GetDonationCreateSerializer(ModelSerializer):
    class Meta:
        model = GetDonation
        queryset = GetDonation.objects.all()
        fields = "__all__"


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        queryset = Comment.objects.all()
        fields = "__all__"

class ImgCreateSerializer(ModelSerializer):
    class Meta:
        model = Img
        queryset = Img.objects.all()
        fields = "__all__"


class SearchGetDonationSerializer(ModelSerializer):
    class Meta:
        model = GetDonation
        fields = "__all__"