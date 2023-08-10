from django.db import models

# Create your models here.
account_list=(
    ('Savings account','Savings account'),
    ('Current account','Current account'),
    ('Joint account ','Joint account'),
)


gender_choice=(
    ('M','Male'),
    ('F','Female'),
    ('O','Others')
)
class District(models.Model):
    objects = None
    name= models.CharField(max_length=150)

    def __str__(self):
         return self.name

class Branch(models.Model):
    objects = None
    name= models.CharField(max_length=150)
    district = models.ForeignKey(District,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class User(models.Model):
    gender_choice = None
    material_choice = None
    account_list = None
    username= models.CharField(max_length=200,unique=True)
    dob= models.DateField(auto_now=False,auto_now_add=False)
    age= models.PositiveIntegerField()
    gender=models.CharField(choices=gender_choice,max_length=100)
    phone=models.PositiveIntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=150)
    district=models.ForeignKey(District,on_delete=models.SET_NULL,blank=True,null=True)
    branch=models.ForeignKey(Branch,on_delete=models.SET_NULL,blank=True,null=True)
    account=models.ManyToManyField('Place')
    material=models.CharField(choices=material_choice,max_length=100)


    def __str__(self):
        return self.username

class Place(models.Model):
    objects = None
    name=models.CharField(max_length=150)