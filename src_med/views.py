from django.shortcuts import render,HttpResponseRedirect
from . import models
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

def home(request):
    return render(request,'index.html',{})

def product(request):
    return render(request,'products.html',{})

def contact(request):
    if request.method=="POST":
        f_name=request.POST["firstname"]
        l_name=request.POST["lastname"]
        phone=request.POST["phone"]
        subject=request.POST["subject"]
        email=request.POST["email"]
        message=request.POST["message"]
        ins=models.contact(first_name=f_name,last_name=l_name,phn_no=phone,subject=subject,email=email,message=message)
        ins.save()
        messages.success(request,"Your response has been submitted successfully!")
        return HttpResponseRedirect('/contact')
    return render(request,'contact.html',{})

def carrer(request):
    
    if request.method=="POST":
        f_name=request.POST["firstname"]
        l_name=request.POST["lastname"]
        phone=request.POST["phone"]
        if request.FILES['resume']:
            resume = request.FILES['resume']
            fs = FileSystemStorage()
            fs.save(resume.name, resume)
        message=request.POST["message"]
        email=request.POST["email"]
        ins=models.carrer(first_name=f_name,last_name=l_name,phn_no=phone,email=email,resume=resume,message=message)
        ins.save()
        messages.success(request,"Your response has been submitted successfully!")
        return HttpResponseRedirect('/carrer')
    return render(request,'carrer.html',context={})

def about_us(request):
    return render(request,'aboutus.html',{})


