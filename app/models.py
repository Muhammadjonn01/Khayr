from django.db import models
from accounts.models import CustomUser


class GetDonation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    like = models.IntegerField(default=0)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=3)
    current_amount = models.DecimalField(max_digits=10, decimal_places=3)
    start_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class Donation(models.Model):
    getdonation = models.ForeignKey(GetDonation,on_delete=models.CASCADE)
    description = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    donation_amount = models.DecimalField(max_digits=10, decimal_places=3)
    donation_date = models.DateField(auto_now_add=True)
    like = models.IntegerField(default=0)
    is_anonymous = models.BooleanField(default=False)
    

class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField()
    likes = models.IntegerField(default=0) 


class Img(models.Model):
    getdonation = models.ForeignKey(GetDonation, on_delete =models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='media')



