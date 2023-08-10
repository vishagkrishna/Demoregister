from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import  redirect
from django.contrib.auth import authenticate,login
from django.shortcuts import render
from django.http import JsonResponse
from .models import Branch,District,Place
# from .forms import Myform
# Create your views here.



def index(request):
    return render(request,"index.html")
def adds(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password1=request.POST.get('password1')

        if password != password1:
            return HttpResponse("password incorrect")
        else:
            user=User.objects.create_user(username,email,password)
            user.save()
            return redirect('login')
    return render(request,"adds.html")

def loginn (request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('page')
        else:
            return HttpResponse("username or password incorrect")
    return render(request,"login.html")

def forms(request):
    return render(request,'formss.html')

def logout(request):
    logout(request)
    return redirect('login')

def get_branches(request):
    district_id= request.GET.get('district_id')
    branches=Branch.objects.filter(district_id=district_id)
    branch_list= [{"id": branch.id,"name": branch.name}for branch in branches]
    return JsonResponse(branch_list,safe=False)

def formss(request):
    district=District.objects.all()
    place=Place.objects.all()
    return render(request,'formss.html',{'district':district,'place':place})

def submit_form(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        dob=request.POST.get('dob')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        address=request.POST.get('address')
        account=request.POST.getlist('account')
        material=request.POST.get('material')

        user= User(username=username,dob=dob,age=age,gender=gender,phone=phone,email=email,address=address,account=account,material=material)
        user.save()
        return redirect('formss')

def final(request):
    return render(request,'final.html')

def home(request):
    return render(request,'home.html')

def navigation_bar(request):
    district= District.objects.all()
    return render(request,'nav.html',{'district':district})
def page(request):
    return render(request,'page.html')