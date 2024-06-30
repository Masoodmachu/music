from django.contrib import auth, messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from music.models import music,event,message,CustomUser,category
# Create your views here.

def index(request):
    m=music.objects.all()
    k = category.objects.all()

    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        ms=request.POST['message']

        form=message.objects.create(name=name,email=email,subject=subject,message=ms)
        form.save()

    return render(request,'index.html',{'m':m,'k':k})

def hindi(request):
    m = music.objects.filter(category='2')
    return render(request,"besthindi.html",{'m':m})



def thamil(request):
    m = music.objects.filter(category='4')
    return render(request,"bestthamil.html",{'m':m})



def malayalam(request):
    m = music.objects.filter(category='3')
    return render(request,"bestmalayalam.html",{'m': m})

def english(request):
    m = music.objects.filter(category='5')
    return render(request,"bestenglish.html",{'m':m})


def events(request):
    e=event.objects.all()

    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        ms=request.POST['message']

        form=message.objects.create(name=name,email=email,subject=subject,message=ms)
        form.save()


    return render(request,"event.html",{'e':e})

def login(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('music:home')
        else:
            return HttpResponse ("Invalid User name Or Password")
    return render(request,"login.html")

def register(request):

    if(request.method=='POST'):
        name=request.POST['name']
        age=request.POST['age']
        phonenumber=request.POST['phonenumber']
        address=request.POST['address']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']

        if confirmpassword==password:
            u=CustomUser.objects.create_user(first_name=name,age=age,phone=phonenumber,address=address,email=email,password=password,username=username)
            u.save()
            return redirect('music:login')
        else:
            return HttpResponse("Invalid username or Password")
    return render(request,"register.html")


def logout(request):
    auth.logout(request)
    return register(request)


def album(request):
    m=category.objects.all()

    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        ms=request.POST['message']

        form=message.objects.create(name=name,email=email,subject=subject,message=ms)
        form.save()

    return render(request,"albums-store.html",{'m':m})

def detail(request,id):
    p=category.objects.get(id=id)
    k=music.objects.filter(category=p)
    return render(request,"detail.html",{'m':k})


def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        ms=request.POST['message']

        form=message.objects.create(name=name,email=email,subject=subject,message=ms)
        form.save()
    return render(request,"contact.html")


def blog(request):
    e=event.objects.all()

    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        ms=request.POST['message']

        form=message.objects.create(name=name,email=email,subject=subject,message=ms)
        form.save()
    return render(request,"blog.html",{'m':e})

def dt(request,id):
    m=music.objects.get(id=id)
    return render(request,"dt.html",{'m':m})