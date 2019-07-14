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
    data=school_data.Details
    dump_data=json.dumps(data)

    for i in dump_data:
        add=i
    return HttpResponse(dump_data)

    # school_details["principle's Name"]= data["school"]["about"]["principle"]
    # school_details["School's Medium"]=data.Details["school"]["about"]["school_details"]["medium"]
    # school_details["School's id"]= school_data.Details["school"]["about"]["school_details"]["school_id"]
    # school_details["No_of_Teachers"]=school_data.Details["school"]["about"]["school_details"]["No_of_teacher"]
    # school_details["NO_of_Students"]=school_data.Details["school"]["about"]["school_details"]["NO_of_students"]
    # school_details["last examination date"]=school_data.Details["school"]["about"]["school_details"]["Last_examination"]
    # school_details["Established year"]=school_data.Details["school"]["about"]["school_details"]["Esatablished_year"]
    # res="Deatails of the school: <br><br>"
    
            
    


