from django.contrib import admin
from .models import User,Branch,District,Place
# Register your models here.
admin.site.register(Branch)
admin.site.register(District)
admin.site.register(User)
admin.site.register(Place)
# class UserModelAdmin(admin.ModelAdmin):
#     list_display = ['id','username','dob','dob','age','gender','phone','email','address','district','branch','account','material']
