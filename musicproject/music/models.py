from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class category(models.Model):
    id=models.IntegerField(primary_key=True)
    image=models.ImageField(upload_to='media/image',blank=True,null=True)
    name=models.CharField(max_length=30)
    desc=models.CharField(max_length=400)
    def __str__(self):
        return self.name


class music(models.Model):
    image=models.ImageField(upload_to='media/image',null=True,blank=True)
    name=models.CharField(max_length=30)
    singer=models.CharField(max_length=30)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    audio=models.FileField(upload_to='media/audio')
    music_composer=models.CharField(max_length=300)
    release_date=models.CharField(max_length=35)


    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    phone=models.IntegerField(default=0)
    age=models.IntegerField(default=0)
    address=models.CharField(max_length=150)

    def __str__(self):
        return self.username





class event(models.Model):
    image=models.ImageField(upload_to='media/event',null=True,blank=True)
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=500)
    location=models.CharField(max_length=150)
    date=models.DateTimeField()

    def __str__(self):
        return self.name



class message(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField()
    subject=models.CharField(max_length=500)
    message=models.CharField(max_length=600)
    date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name