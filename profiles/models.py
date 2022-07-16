from django.db import models
from accounts.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user_pk = models.IntegerField(blank=True)
    profile_img = models.ImageField(default="accounts/person.png", upload_to="accounts/", null=True, blank=True)
    intro = models.CharField(max_length=150, blank=True)
    part = models.CharField(max_length=20, blank=True)
    sub_part = models.CharField(max_length=20, blank=True)
    hash_tag = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(upload_to="profile/image", blank=True)
    pup_date = models.DateTimeField(auto_now_add=True)


class Profile_url(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=20, blank=True)
    url = models.URLField(max_length=400, blank=True)


class Proj(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, null=True, blank=True)
    img = models.ImageField(upload_to="proj/image", blank=True)
    title = models.CharField(max_length=50, blank=True)
    body = models.CharField(max_length=100, blank=True)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(blank=True)