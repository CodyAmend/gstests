from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



GENDER = (
    ('M', 'Male'),
    ('F', 'Female')
)

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50,verbose_name="First Name")
    last_name = models.CharField(max_length=50,verbose_name="Last Name")
    gender = models.CharField(max_length=10,verbose_name="Gender", choices=GENDER)
    birth_date = models.DateField(verbose_name="Birth date")
    address = models.CharField(max_length=100,verbose_name="Mailing Address")
    city = models.CharField(max_length=50, verbose_name="City")
    zipcode = models.CharField(max_length=20, verbose_name="Zipcode")
    phone = models.CharField(max_length=10,verbose_name="Phone number")
    is_employed = models.BooleanField(verbose_name="Are you Employed?")
    employer = models.CharField(max_length=50,verbose_name="If currently employed then who is your current employer?", blank=True)
    family_size = models.IntegerField(verbose_name="How many members in the family including you?")
    items_needed = models.TextField(max_length=200,verbose_name="What items do you need today?")
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()