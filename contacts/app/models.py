from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    gender = models.CharField(max_length=50, choices=(('male', 'Male'), ('female', 'Female')), default="Select an Option")
    info = models.CharField(max_length=20)
    #image = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    image = models.ImageField(upload_to='images/',blank=True)
    #date_added = models.DateField(auto_now=False, auto_now_add=False)
    #date_added = models.DateField(auto_now_add=True)
    date_added = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.name

class Meta:
    ordering = ['-id']