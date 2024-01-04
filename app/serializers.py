from rest_framework.serializers import ModelSerializer
from .models  import *



class UserChoiceListSerializer(ModelSerializer):
    class Meta:
        model = UserChoice
        queryset = UserChoice.objects.all()
        fields = "__all__"

class DonationListSerializer(ModelSerializer):
    class Meta:
        model = Donation
        queryset = Donation.objects.all()
        fields = "__all__"

class GetDonationListSerializer(ModelSerializer):
    class Meta:
        model = GetDonation
        queryset = GetDonation.objects.all()
        fields = "__all__"

class CommentListSerializer(ModelSerializer):
    class Meta:
        model = Comment
        queryset = Comment.objects.all()
        fields = "__all__"

class FileListSerializer(ModelSerializer):
    class Meta:
        model = File
        queryset = File.objects.all()
        fields = "__all__"


class UserChoiceCreateSerializer(ModelSerializer):
    class Meta:
        model = UserChoice
        queryset = UserChoice.objects.all()
        fields = "__all__"

class DonationCreateSerializer(ModelSerializer):
    class Meta:
        model = Donation
        queryset = Donation.objects.all()
        fields = "__all__"


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

class FileCreateSerializer(ModelSerializer):
    class Meta:
        model = File
        queryset = File.objects.all()
        fields = "__all__"
