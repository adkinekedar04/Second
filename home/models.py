
from distutils.command.upload import upload
from statistics import mode
from django.db import models

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class Register(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=20)
    # date = models.DateField()

    def __str__(self):
        return self.name

class Event(models.Model):
    collegename = models.CharField(max_length=122,default ="")
    eventname = models.CharField(max_length=122,default ="")
    date = models.DateField()
    desc = models.TextField()
    image = models.ImageField(upload_to ="home/images" ,default ="")
    def __str__(self):
        return self.collegename

class Profile(models.Model):
    profilename = models.CharField(max_length=122,default ="")
    profileemail = models.CharField(max_length=122,default ="")
    profilenumber = models.CharField(max_length=122,default="")
    profilecollege = models.CharField(max_length=122,default ="")
    branch = models.CharField(max_length=122,default ="")
    profiledesc = models.TextField()
    profileimage = models.ImageField(upload_to ="home/profile/images" ,default ="")
    def __str__(self):
        return self.profilename