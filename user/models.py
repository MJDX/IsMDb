from django.contrib.auth.models import User
from django.db import models
from django_countries.fields import CountryField


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    models.ImageField(default='default.jpg', upload_to='profile_pics')
    country = CountryField(default='US', null=False)
    birthday_date = models.DateField
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'))
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    honor_points = models.IntegerField(default=0)
