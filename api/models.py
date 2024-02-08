from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    about=models.CharField(max_length=200,null=True,blank=True)
    dob=models.DateField(null=True,blank=True)
    profile_pic=models.ImageField(upload_to="images",default="default.jpg")
    options=[
        ("male","male"),("female","female")
        ]
    gender=models.CharField(max_length=200,choices=options,default="male")

    


def creat_profile(sender,instance,created,**kwargs):
    if created and not instance.is_superuser:
        Profile.objects.create(user=instance)

post_save.connect(creat_profile,sender=User)