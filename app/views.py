from django.shortcuts import render
from app.models import *
from django.http import HttpResponse,HttpResponseNotFound 
import json

# Create your views here.
def SignupForm(request):
    return render(request,"app/signup.html")

def hello(request):
    import datetime
    today = datetime.datetime.now().date()
    day_of_week=["monday","tuesday","wdnesday","thursday","friday","saturday","sunday"]
    return render(request, "app/app.html", {"today" : today,"days_of_week":day_of_week})

#for rendiring the user names from userdetails models
def crudops(request):

    #read all enteries
    objects=UserDetail.objects.all()
    res="Printing all details from the database: <br>"

    for elt in objects:
        res+=elt.name + " " + elt.website+" "+str(elt.phonenumber) +"<br>"
    
    return HttpResponse(res)

def list_of_school(request):
    # reading data of schools
    school_data=School.objects.all()
    res="List of all the Schools are: <br><br>"
    num=1
    for school in school_data:
        res+=str(num)+": "+school.SchoolName+"<br>"+"Address :   "+school.Address +"<br><br>"
        num+=1
    return HttpResponse(res)

#deatils of a school

def SchoolDetails(response,id):
    school_data=School.objects.get(pk=id)
    name=school_data.SchoolName
    address=school_data.Address
    data=school_data.Details
    dump_data=json.dumps(data)
    return HttpResponse("School Name :- {} <br> School Address:-{} <br> School Details :-{}".format(name,address,dump_data))


   
    
    
            
    


