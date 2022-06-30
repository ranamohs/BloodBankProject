from django.shortcuts import render
from . import models

# Create your views here.

def home1 (request):
    return render(request , 'home1.html' , {})


def login (request):
    return render(request , 'login.html' , {})




def backend1(request):
    v1 = request.POST['username']
    v2 = request.POST['password']
    new = models.login()
    new.email = v1 
    new.password = v2
    new.save()
    return render (request , 'home2.html ' , {})


def home2 (request):
    return render(request , 'home2.html' , {})


def signup (request):
    return render(request , 'signup.html' , {})




def backend2(request):
    v1 = request.POST['Firstname']
    v2 = request.POST['Secondname']
    v3 = request.POST['username']
    v4 = request.POST['password']
    v5 = request.POST['repassword']
    v6 = request.POST['Phone']
    new = models.signup()
    new.first_name = v1 
    new.second_name = v2
    new.email = v3
    new.Password = v4
    new.re_Password = v5 
    new.phone = v6
    new.save()
    return render (request , 'login.html ' , {})

    

def bloodbank (request):
    return render(request , 'Reach_to_bloodbank.html' , {})



def requests (request):
    return render(request , 'Donerrequest.html' , {})




def donorr (request):
    return render(request , 'Log in as a donor.html' , {})




def backend3(request):
    v1 = request.POST['Yourname']
    v2 = request.POST['username']
    v3 = request.POST['blood']
    v4 = request.POST['The state']
    v5 = request.POST['city']
    v6 = request.POST['Phone']
    v7 = request.POST['APhone']
    v8 = request.POST['Gender']
    v9 = request.POST['Cdiseases']
    v10 = request.POST['diseases']
    
    new = models.Donor()
    new.name = v1 
    new.email = v2
    new.donor_blood = v3
    new.The_State = v4 
    new.city = v5
    new.Phone = v6
    new.Another_Phone = v7
    new.Gender = v8
    new.Anychronicdiseases = v9
    new.Getting_Dentist_Recently = v10
    new.save()
    return render (request , 'home2.html ' , {})


def needyy (request):
    return render(request , 'Search.html' , {})

def backend4(request):
    v1 = request.POST['name']
    v2 = request.POST['type']
    v3 = request.POST['number']
    v4 = request.POST['hospitalname']
    v5 = request.POST['country']
    v6 = request.POST['city']
    v7 = request.POST['date']
    v8 = request.POST['Fphone']
    v9 = request.POST['Sphone']
    v10 = request.POST['details']
   
    
    new = models.needy()
    new.name_or_file_number_of_the_patient = v1 
    new.Required_blood_type = v2
    new.Number_of_units_required = v3
    new.Hospital_Name = v4 
    new.Country = v5
    new.city = v6
    new.Date = v7
    new.First_Phone_Number = v8
    new.Second_Phone_Number = v9
    new.Other_Details = v10
    new.save()
    return render (request , 'home2.html ' , {})



def searchh (request):
    return render(request , 'Reach_to_bloodbank.html' , {})

def backend5(request):
   
    v1 = request.POST['country']
    v2 = request.POST['city']
   
   
    
    new = models.search()
    new.Country = v1
    new.city = v2
    new.save()
    return render (request , 'Donerrequest.html ' , {})


def Notf (request):
    return render(request , 'notifications.html' , {})




