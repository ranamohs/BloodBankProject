from random import choices
from django.db import models


# Create your models here.



class login(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=100)



class signup(models.Model):
    first_name= models.CharField(max_length=100)
    second_name= models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=100)
    re_Password = models.CharField(max_length=100)
    phone = models.IntegerField()








class Donor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    donor_blood = models.CharField(max_length=2)
    The_State = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    Phone = models.CharField(max_length=15)
    Another_Phone = models.CharField(max_length=15)
    Gender = models.CharField(max_length=6)
    Anychronicdiseases = models.CharField(max_length=3)
    Getting_Dentist_Recently = models.CharField(max_length=3)



class needy(models.Model):
    name_or_file_number_of_the_patient= models.CharField(max_length=100)
    Required_blood_type = models.CharField(max_length=100 )
    Number_of_units_required = models.IntegerField ()
    Hospital_Name= models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    Date = models.DateTimeField(auto_now=True)
    First_Phone_Number = models.CharField(max_length=14)
    Second_Phone_Number = models.CharField(max_length=14)
    Other_Details = models.CharField(max_length=100)


class search(models.Model):
    Country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    