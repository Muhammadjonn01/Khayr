from django.db import models
from accounts.models import CustomUser

class ConstFields:
    post_category = (
        ('Donate', 'Donate'),
        ('Get Donation', 'Get Donation'),
    )

class UserChoice(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=ConstFields.post_category, default=None)

class GetDonation(models.Model):
    userchoice = models.ForeignKey(UserChoice,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    like = models.IntegerField(default=0)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=3)
    current_amount = models.DecimalField(max_digits=10, decimal_places=3)
    start_date = models.DateField(auto_now_add=True)

class Donation(models.Model):
    userchoice = models.ForeignKey(UserChoice,on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    userchoice = models.ForeignKey(UserChoice, on_delete=models.CASCADE)
    donation_amount = models.DecimalField(max_digits=10, decimal_places=3)
    donation_date = models.DateField(auto_now_add=True)
    is_anonymous = models.BooleanField(default=False)

class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    userchoice = models.ForeignKey(UserChoice, on_delete=models.CASCADE)
    comment = models.TextField()
    likes = models.IntegerField(default=0) 


class File(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to='media')



