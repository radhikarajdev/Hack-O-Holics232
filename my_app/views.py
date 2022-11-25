from django.shortcuts import render
from django.views import View
import csv
from csv import writer

# Create your views here.
class Signup(View):
    def get(self,request):
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=[username,password]
            with open('user.csv','a') as myfile:
                writer_object=writer(myfile)
                writer_object.writerow(user)
                myfile.close()

        return render(request,'signup.html')

class Login(View):
    def get(self, request):
        if request.method=="POST":
            username=request.POST['username']
            password=request.POST['password']
            user=[username,password]
            myfile=open("user.csv",'a')
            data=myfile.readlines()
            if user in data:
                pass
        return render(request,'login.html')

class Dashboard(View):
    def get(self, request):
        return render(request, 'dashboard.html')

class Test(View):
    def get(self,request):
        if request.method=="POST":
            global chosen
            chosen=request.POST.getlist('checks[]')

        return render(request,'test.html')
class Contactus(View):
    def get(self,request):
        return render(request,'contactus.html')

