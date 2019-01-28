from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)

    # additional to user model
    # blank means isn't required
    portfolio_site = models.URLField(blank=True)
    # save pics under media\profile_pics\
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    def __str__(self):
        return self.user.username
